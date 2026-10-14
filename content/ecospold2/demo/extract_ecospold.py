#!/usr/bin/env python3
"""Read EcoSpold02 records; no formula evaluation, allocation or network calculation.

Standard library only. Run: python extract_ecospold.py INPUT --out OUTPUT
--kind is a user-supplied stage label; activity type 1/2 never sets it implicitly.
CSV amounts retain their original XML strings. Decimal ratios are supplementary.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation, localcontext
import json
import re
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

NS = 'http://www.EcoInvent.org/EcoSpold02'
XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'
NUMERIC = {'amount', 'productionVolumeAmount', 'meanValue', 'mu', 'variance',
           'varianceWithPedigreeUncertainty', 'minValue', 'maxValue',
           'mostLikelyValue', 'mostFrequentValue', 'standardDeviation95',
           'shape', 'scale', 'n', 'p'}


def q(name):
    return '{' + NS + '}' + name


def number(raw, location):
    if raw is None or not raw.strip():
        raise ValueError(f'{location}: missing numeric amount/value; not replaced with 0')
    try:
        value = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError(f'{location}: invalid decimal {raw!r}') from exc
    if not value.is_finite():
        raise ValueError(f'{location}: non-finite decimal {raw!r}')
    if re.fullmatch(r'[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?', raw.strip()) is None:
        raise ValueError(f'{location}: invalid XML decimal lexical form {raw!r}')
    return value


def required_attr(node, name, location):
    value = node.get(name)
    if value is None or not value.strip():
        raise ValueError(f'{location}: missing required attribute {name}')
    return value


def one(parent, name, required=False):
    nodes = parent.findall(q(name))
    if len(nodes) > 1:
        raise ValueError(f'{name}: duplicate singleton element ({len(nodes)})')
    if not nodes:
        if required:
            raise ValueError(f'missing required element {name}')
        return None
    return nodes[0]


def tree(node):
    """Keep raw attributes, text, namespace-qualified tags and repeated children."""
    return {'tag': node.tag, 'attributes': dict(node.attrib), 'text': node.text,
            'children': [tree(child) for child in list(node)]}


def texts(node, name):
    return [{'language': x.get(XML_LANG), 'text': x.text,
             'attributes': dict(x.attrib)} for x in node.findall(q(name))]


def select(values, language, default):
    for wanted in (language, default):
        for value in values:
            if value['language'] == wanted:
                return value['text']
        for value in values:
            if value['language'] is not None and value['language'].split('-')[0] == wanted:
                return value['text']
    return values[0]['text'] if values else None


def effective(raw, dataset_context):
    return dataset_context if raw is None else raw


def release_number(raw, location):
    if raw is None or not raw.strip():
        return None
    if re.fullmatch(r'[+-]?[0-9]+', raw.strip()) is None:
        raise ValueError(f'{location}: invalid XML integer release {raw!r}')
    return int(raw)


def supplier_compatibility(request, candidate):
    """Require known equal model and database release; never choose by revision."""
    requested_model = request['system_model'] or {}
    candidate_model = candidate['system_model'] or {}
    pairs = [('systemModelId', requested_model.get('id'), candidate_model.get('id')),
             ('systemModelContextId', requested_model.get('context_id'), candidate_model.get('context_id')),
             ('majorRelease', request['database_release']['major_release'], candidate['database_release']['major_release']),
             ('minorRelease', request['database_release']['minor_release'], candidate['database_release']['minor_release'])]
    reasons = []
    missing = False
    mismatch = False
    for name, wanted, actual in pairs:
        if wanted is None or wanted == '' or actual is None or actual == '':
            missing = True
            reasons.append({'field': name, 'reason': 'unknown', 'requested': wanted, 'candidate': actual})
        elif wanted != actual:
            mismatch = True
            reasons.append({'field': name, 'reason': 'different', 'requested': wanted, 'candidate': actual})
    return ('incompatible' if mismatch else ('unknown' if missing else 'compatible')), reasons


def direction(node, kind):
    ig = one(node, 'inputGroup')
    og = one(node, 'outputGroup')
    if (ig is None) == (og is None):
        raise ValueError('exchange direction requires exactly one inputGroup or outputGroup; sign is not used')
    group = ig if ig is not None else og
    raw = group.text
    if raw is None:
        raise ValueError('empty flow-direction group')
    if re.fullmatch(r'[+-]?[0-9]+', raw.strip()) is None:
        raise ValueError(f'invalid XML integer flow-direction group {raw!r}')
    try:
        code = int(raw)
    except ValueError as exc:
        raise ValueError(f'invalid flow-direction group {raw!r}') from exc
    permitted = ({1, 2, 3, 5} if ig is not None else {0, 2, 3, 5}) if kind == 'intermediateExchange' else {4}
    if code not in permitted:
        raise ValueError(f'invalid {kind} flow-direction group {raw!r}')
    return ('input' if ig is not None else 'output'), raw, code


def ratio(raw, reference):
    if reference is None:
        return None
    with localcontext() as ctx:
        ctx.prec = 50
        return format(number(raw, 'normalization') / reference, 'f')


def extract(paths, language='zh', kind='unknown'):
    if language not in {'zh', 'en'} or kind not in {'upr', 'lci', 'lcia', 'unknown'}:
        raise ValueError('unsupported language or kind')
    result = {'metadata': [], 'exchanges': [], 'parameters': [], 'properties': [],
              'impacts': [], 'uncertainty': [], 'supplier-links': []}
    for path in paths:
        path = Path(path)
        root = ET.parse(path).getroot()
        if root.tag != q('ecoSpold'):
            raise ValueError(f'{path}: wrong root/namespace; expected {q("ecoSpold")}')
        datasets = []
        for child in list(root):
            local = child.tag.rsplit('}', 1)[-1]
            if local == 'childActivityDataset':
                raise ValueError(f'{path}: childActivityDataset requires inheritance expansion before extraction (需先展开继承)')
            if child.tag == q('activityDataset'):
                datasets.append(child)
            elif local == 'activityDataset':
                raise ValueError(f'{path}: wrong activityDataset namespace')
        if not datasets:
            raise ValueError(f'{path}: no activityDataset')
        for index, ds in enumerate(datasets):
            key = f'{path.as_posix()}#{index}'
            desc = one(ds, 'activityDescription', True)
            flow = one(ds, 'flowData', True)
            modelling = one(ds, 'modellingAndValidation', True)
            admin = one(ds, 'administrativeInformation', True)
            activity = one(desc, 'activity', True)
            geo = one(desc, 'geography', True)
            period = one(desc, 'timePeriod', True)
            fa = one(admin, 'fileAttributes', True)
            rep = one(modelling, 'representativeness')
            context = fa.get('contextId')
            default = fa.get('defaultLanguage', 'en')
            aid = required_attr(activity, 'id', key)
            names = texts(activity, 'activityName')
            meta = {'dataset_key': key, 'file': path.as_posix(), 'dataset_index': index,
                    'activity_id': aid, 'activity_type': activity.get('type'),
                    'kind': kind, 'context_id': context, 'default_language': default,
                    'name': select(names, language, default), 'names': names,
                    'geography': {'attributes': dict(geo.attrib), 'shortnames': texts(geo, 'shortname')},
                    'time_period': dict(period.attrib),
                    'system_model': None if rep is None else {'id': rep.get('systemModelId'),
                                      'context_id': effective(rep.get('systemModelContextId'), context),
                                      'attributes': dict(rep.attrib), 'names': texts(rep, 'systemModelName')},
                    'database_release': {'major_release': release_number(fa.get('majorRelease'), key),
                                         'minor_release': release_number(fa.get('minorRelease'), key),
                                         'raw_major_release': fa.get('majorRelease'), 'raw_minor_release': fa.get('minorRelease')},
                    'dataset_revision': {'major_revision': fa.get('majorRevision'), 'minor_revision': fa.get('minorRevision')},
                    'raw_sections': {n: tree(x) for n, x in [('activityDescription', desc), ('modellingAndValidation', modelling), ('administrativeInformation', admin)]}}
            # Validate finite lexical numeric values everywhere while keeping raw strings.
            for node in ds.iter():
                for attr, value in node.attrib.items():
                    if attr in NUMERIC:
                        number(value, f'{key}/{node.tag}/{attr}')
            rows = []
            uncertainty_items = []

            def record(node, owner_kind, owner_index):
                raw = required_attr(node, 'amount', f'{key}/{owner_kind}/{owner_index}')
                number(raw, f'{key}/{owner_kind}/{owner_index}/amount')
                names = texts(node, 'name')
                units = texts(node, 'unitName')
                row = {'dataset_key': key, 'activity_id': aid, 'context_id': context,
                       'record_index': owner_index, 'name': select(names, language, default),
                       'names': names, 'amount': raw,
                       'unit_name': select(units, language, default), 'unit_names': units,
                       'unit_id': node.get('unitId'),
                       'unit_context_id': None if owner_kind == 'impactIndicator' else effective(node.get('unitContextId'), context),
                       'xml_attributes': dict(node.attrib), 'raw_children': [tree(x) for x in list(node)]}
                for u_name in ('uncertainty', 'productionVolumeUncertainty'):
                    u = one(node, u_name)
                    if u is not None:
                        uncertainty_items.append({'dataset_key': key, 'owner_kind': owner_kind,
                                                  'owner_index': owner_index, 'owner_id': node.get('id', node.get('parameterId', node.get('propertyId'))),
                                                  'field': u_name, 'raw': tree(u)})
                return row

            for node in list(flow):
                if node.tag in (q('intermediateExchange'), q('elementaryExchange')):
                    ex_kind = node.tag.rsplit('}', 1)[-1]
                    row = record(node, ex_kind, len(rows))
                    row['exchange_kind'] = ex_kind
                    row['exchange_id'] = required_attr(node, 'id', key)
                    master = 'intermediateExchange' if ex_kind == 'intermediateExchange' else 'elementaryExchange'
                    row['flow_id'] = required_attr(node, master + 'Id', key)
                    row['flow_context_id'] = effective(node.get(master + 'ContextId'), context)
                    required_attr(node, 'unitId', key)
                    row['direction'], row['group'], row['group_code'] = direction(node, ex_kind)
                    row['activity_link_id'] = node.get('activityLinkId')
                    row['activity_link_context_id'] = effective(node.get('activityLinkContextId'), context)
                    row['production_volume_amount'] = node.get('productionVolumeAmount')
                    comp = one(node, 'compartment', ex_kind == 'elementaryExchange')
                    row['compartment'] = None if comp is None else select(texts(comp, 'compartment'), language, default)
                    row['subcompartment'] = None if comp is None else select(texts(comp, 'subcompartment'), language, default)
                    row['subcompartment_id'] = None if comp is None else comp.get('subcompartmentId')
                    row['subcompartment_context_id'] = None if comp is None else effective(comp.get('subcompartmentContextId'), context)
                    rows.append(row)
                    for prop_index, prop in enumerate(node.findall(q('property'))):
                        pr = record(prop, 'property', f'{row["record_index"]}:{prop_index}')
                        pr.update(exchange_id=row['exchange_id'], property_id=required_attr(prop, 'propertyId', key),
                                  property_context_id=effective(prop.get('propertyContextId'), context))
                        result['properties'].append(pr)
                elif node.tag == q('parameter'):
                    pr = record(node, 'parameter', len(result['parameters']))
                    pr.update(parameter_id=required_attr(node, 'parameterId', key),
                              parameter_context_id=effective(node.get('parameterContextId'), context),
                              variable_name=node.get('variableName'))
                    result['parameters'].append(pr)
                elif node.tag == q('impactIndicator'):
                    ir = record(node, 'impactIndicator', len(result['impacts']))
                    for part in ('impactMethod', 'impactCategory', 'impactIndicator'):
                        ir[part + 'Id'] = required_attr(node, part + 'Id', key)
                        ir[part + 'ContextId'] = effective(node.get(part + 'ContextId'), context)
                    ir['impact_method_names'] = texts(node, 'impactMethodName')
                    ir['impact_category_names'] = texts(node, 'impactCategoryName')
                    result['impacts'].append(ir)
                elif node.tag.rsplit('}', 1)[-1] in {'intermediateExchange', 'elementaryExchange', 'parameter', 'impactIndicator'}:
                    raise ValueError(f'{key}: wrong flowData namespace: {node.tag}')
                elif node.tag.startswith('{' + NS + '}'):
                    raise ValueError(f'{key}: unsupported flowData element {node.tag}')
            refs = [row for row in rows if row['exchange_kind'] == 'intermediateExchange' and row['direction'] == 'output' and row['group_code'] == 0]
            reference = None
            if len(refs) != 1:
                status = 'no-reference' if not refs else 'multiple-references'
            else:
                value = number(refs[0]['amount'], key)
                status = 'zero-reference' if value == 0 else ('negative-reference' if value < 0 else 'unique-positive-reference')
                if value > 0:
                    reference = value
            meta['normalization'] = {'status': status, 'reference_exchange_id': refs[0]['exchange_id'] if len(refs) == 1 else None,
                                     'reference_amount': refs[0]['amount'] if len(refs) == 1 else None,
                                     'reference_unit_id': refs[0]['unit_id'] if len(refs) == 1 else None,
                                     'decimal_precision': 50, 'scope': 'Arithmetic ratio only; no allocation or LCI/LCIA calculation.'}
            for row in rows:
                row['normalization_status'] = status
                row['normalized_amount'] = ratio(row['amount'], reference)
            for row in result['impacts']:
                if row['dataset_key'] == key:
                    row['normalization_status'] = status
                    row['normalized_amount'] = ratio(row['amount'], reference)
            result['metadata'].append(meta)
            result['exchanges'].extend(rows)
            result['uncertainty'].extend(uncertainty_items)
    # Match exported candidates only. Keep repeated outputs and datasets distinct.
    metadata = {x['dataset_key']: x for x in result['metadata']}
    outputs = [x for x in result['exchanges'] if x['exchange_kind'] == 'intermediateExchange' and x['direction'] == 'output']
    for row in result['exchanges']:
        if row['exchange_kind'] != 'intermediateExchange' or row['direction'] != 'input':
            continue
        link = row['activity_link_id']
        candidates = []
        if link is None or link == '':
            status = 'unlinked'
        elif row['activity_link_context_id'] is None or row['flow_context_id'] is None:
            status = 'context-unavailable'
        else:
            identity_candidates = [x for x in outputs if x['activity_id'] == link and
                                   (x['context_id'] is None or x['context_id'] == row['activity_link_context_id']) and
                                   x['flow_id'] == row['flow_id'] and
                                   (x['flow_context_id'] is None or x['flow_context_id'] == row['flow_context_id'])]
            for candidate in identity_candidates:
                meta = metadata[candidate['dataset_key']]
                compatibility, reasons = supplier_compatibility(metadata[row['dataset_key']], meta)
                for field in ('context_id', 'flow_context_id'):
                    if candidate[field] is None:
                        reasons.append({'field': 'candidate_' + field, 'reason': 'unknown',
                                        'requested': row['activity_link_context_id'] if field == 'context_id' else row[field],
                                        'candidate': None})
                        if compatibility != 'incompatible':
                            compatibility = 'unknown'
                candidates.append({'dataset_key': candidate['dataset_key'], 'exchange_id': candidate['exchange_id'],
                                   'amount': candidate['amount'], 'unit_id': candidate['unit_id'],
                                   'unit_context_id': candidate['unit_context_id'],
                                   'unit_matches_request': candidate['unit_id'] == row['unit_id'] and candidate['unit_context_id'] == row['unit_context_id'],
                                   'compatibility': compatibility, 'compatibility_reasons': reasons,
                                   'metadata': {k: meta[k] for k in ('activity_id', 'context_id', 'system_model', 'database_release',
                                                                   'dataset_revision', 'geography', 'time_period')}})
            compatible = [x for x in candidates if x['compatibility'] == 'compatible']
            unknown = [x for x in candidates if x['compatibility'] == 'unknown']
            if not candidates:
                status = 'not-in-export'
            elif len(compatible) > 1:
                status = 'ambiguous'
            elif unknown:
                status = 'metadata-unconfirmed'
            elif len(compatible) == 1:
                status = 'matched'
            else:
                status = 'incompatible-metadata'
        result['supplier-links'].append({'dataset_key': row['dataset_key'], 'exchange_id': row['exchange_id'],
                                         'activity_link_id': link, 'activity_link_context_id': row['activity_link_context_id'],
                                         'flow_id': row['flow_id'], 'flow_context_id': row['flow_context_id'], 'status': status,
                                         'candidates': candidates,
                                         'scope': 'Candidates in this export only; no traversal or network calculation.'})
    return result


def write_outputs(result, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    for name in ('metadata', 'uncertainty', 'supplier-links'):
        (out / (name + '.json')).write_text(json.dumps(result[name], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name in ('exchanges', 'parameters', 'properties', 'impacts'):
        rows = result[name]
        columns = list(dict.fromkeys(k for row in rows for k in row))
        if not columns:
            columns = ['dataset_key', 'amount']
        with (out / (name + '.csv')).open('w', encoding='utf-8-sig', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            for row in rows:
                writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in row.items()})


def discover(inputs):
    files = []
    for value in inputs:
        p = Path(value)
        if p.is_dir():
            files.extend(x for x in sorted(p.rglob('*')) if x.is_file() and x.suffix.lower() in {'.xml', '.spold'})
        elif p.is_file():
            files.append(p)
        else:
            raise ValueError(f'input path does not exist: {p}')
    files = list(dict.fromkeys(x.resolve() for x in files))
    if not files:
        raise ValueError('no XML or .spold input files found')
    return files


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs='+', help='XML/.spold files or recursively searched directories')
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--language', choices=['zh', 'en'], default='zh')
    parser.add_argument('--kind', choices=['upr', 'lci', 'lcia', 'unknown'], default='unknown')
    args = parser.parse_args(argv)
    try:
        result = extract(discover(args.inputs), args.language, args.kind)
        write_outputs(result, args.out)
    except (ValueError, ET.ParseError, OSError) as exc:
        print(f'Extraction failed: {exc}', file=sys.stderr)
        return 2
    print(f'Extracted {len(result["metadata"])} dataset(s), {len(result["exchanges"])} exchange(s) into {args.out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run: python -m unittest discover -s tools -p test_ecospold_tutorial.py -v.
lxml is used only for official schema validation; extraction uses stdlib only.
"""
import copy
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / 'content/ecospold2/demo'
spec = importlib.util.spec_from_file_location('extractor', DEMO / 'extract_ecospold.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
Q = e.q


class TutorialTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.result = e.extract(sorted(DEMO.glob('*.spold')))

    def modified(self, change):
        root = ET.parse(DEMO / 'demo-product.spold').getroot()
        change(root)
        p = self.dir / 'changed.spold'
        ET.ElementTree(root).write(p, encoding='utf-8', xml_declaration=True)
        return p

    def product(self):
        return [x for x in self.result['exchanges'] if 'demo-product.spold#' in x['dataset_key']]

    def test_official_schema(self):
        from lxml import etree
        schema_dir = DEMO.parent / 'original/Schemas'
        class Resolver(etree.Resolver):
            def resolve(self, url, pubid, context):
                if Path(url).name == 'XmlNamespace.xsd':
                    return self.resolve_filename(str(schema_dir / 'XmlNamespace.xsd'), context)
        parser = etree.XMLParser(no_network=True)
        parser.resolvers.add(Resolver())
        schema = etree.XMLSchema(etree.parse(str(schema_dir / 'datasets/EcoSpold02.xsd'), parser))
        for p in DEMO.glob('*.spold'):
            schema.assertValid(etree.parse(str(p), parser))
            ds = ET.parse(p).getroot().find(Q('activityDataset'))
            self.assertEqual([x.tag for x in ds], [Q(n) for n in ['activityDescription', 'flowData', 'modellingAndValidation', 'administrativeInformation']])
            for n in ['dataEntryBy', 'dataGeneratorAndPublication']:
                self.assertEqual(ds.find('.//' + Q(n)).get('personEmail'), 'demo@example.invalid')
        self.assertEqual({m['activity_type'] for m in self.result['metadata']}, {'1', '2'})
        self.assertEqual({m['kind'] for m in self.result['metadata']}, {'unknown'})

    def test_signed_identity_and_direct_inventory(self):
        fossil = [x for x in self.product() if x['name'] == '二氧化碳，化石源（教学）']
        self.assertEqual(len(fossil), 2)
        self.assertEqual({x['direction'] for x in fossil}, {'output'})
        self.assertEqual({x['amount'] for x in fossil}, {'1.5', '-0.1'})
        self.assertEqual(len({x['exchange_id'] for x in fossil}), 2)
        self.assertEqual(len({x['flow_id'] for x in fossil}), 1)
        self.assertEqual(len({x['subcompartment_id'] for x in fossil}), 1)
        self.assertEqual(sum(Decimal(x['amount']) for x in fossil), Decimal('1.4'))
        self.assertEqual(sum(Decimal(x['normalized_amount']) for x in fossil), Decimal('0.14'))
        def same_names(root):
            for ex in root.findall('.//' + Q('elementaryExchange')):
                for name in ex.findall(Q('name')):
                    name.text = 'same display name'
        rows = e.extract([self.modified(same_names)])['exchanges']
        co2 = [x for x in rows if x['xml_attributes'].get('formula') == 'CO2']
        self.assertEqual(len(co2), 3)
        self.assertEqual(len({x['flow_id'] for x in co2}), 2)

    def test_ratios_and_unscaled_values(self):
        elec = next(x for x in self.product() if x['direction'] == 'input' and x['group_code'] == 2)
        water = next(x for x in self.product() if x['direction'] == 'input' and x['group_code'] == 4)
        self.assertEqual(elec['normalized_amount'], '2.5')
        self.assertEqual(water['normalized_amount'], '0.004')
        self.assertEqual(self.result['parameters'][0]['amount'], '2.5')
        self.assertEqual(self.result['properties'][0]['amount'], '1')
        for name in ['parameters', 'properties']:
            self.assertNotIn('normalized_amount', self.result[name][0])
        p = self.modified(lambda root: root.find('.//' + Q('intermediateExchange')).set('productionVolumeAmount', '1234'))
        self.assertEqual(e.extract([p])['exchanges'][0]['production_volume_amount'], '1234')
        attrs = self.result['uncertainty'][0]['raw']['children'][0]['attributes']
        self.assertEqual(attrs, {'meanValue': '25', 'mu': '3.2188758248682006', 'variance': '0.01', 'varianceWithPedigreeUncertainty': '0.04'})

    def test_supplier_status_and_context(self):
        self.assertEqual(self.result['supplier-links'][0]['status'], 'matched')
        self.assertEqual(e.extract([DEMO / 'demo-product.spold'])['supplier-links'][0]['status'], 'not-in-export')
        def unlink(root):
            del root.findall('.//' + Q('intermediateExchange'))[1].attrib['activityLinkId']
        self.assertEqual(e.extract([self.modified(unlink)])['supplier-links'][0]['status'], 'unlinked')
        files = [DEMO / n for n in ['demo-product.spold', 'demo-electricity.spold', 'demo-electricity.spold']]
        self.assertEqual(e.extract(files)['supplier-links'][0]['status'], 'ambiguous')
        p = self.modified(lambda root: root.findall('.//' + Q('intermediateExchange'))[1].set('activityLinkContextId', '00000000-0000-4000-8000-000000000001'))
        self.assertEqual(e.extract([p, DEMO / 'demo-electricity.spold'])['supplier-links'][0]['status'], 'not-in-export')

    def test_supplier_model_release_and_unknown_metadata(self):
        def supplier(change, filename='supplier.spold'):
            root = ET.parse(DEMO / 'demo-electricity.spold').getroot()
            change(root)
            p = self.dir / filename
            ET.ElementTree(root).write(p, encoding='utf-8', xml_declaration=True)
            return p
        def link(path):
            return e.extract([DEMO / 'demo-product.spold', path])['supplier-links'][0]
        for attribute in ['systemModelId', 'systemModelContextId']:
            with self.subTest(attribute=attribute):
                p = supplier(lambda root: root.find('.//' + Q('representativeness')).set(attribute, '00000000-0000-4000-8000-000000000099'))
                result = link(p)
                self.assertEqual(result['status'], 'incompatible-metadata')
                self.assertEqual(result['candidates'][0]['compatibility_reasons'][0]['field'], attribute)
        for attribute in ['majorRelease', 'minorRelease']:
            with self.subTest(attribute=attribute):
                p = supplier(lambda root: root.find('.//' + Q('fileAttributes')).set(attribute, '99'))
                self.assertEqual(link(p)['status'], 'incompatible-metadata')
        for attribute in ['systemModelId', 'majorRelease', 'minorRelease', 'contextId']:
            with self.subTest(missing=attribute):
                def remove(root):
                    tag = 'representativeness' if attribute == 'systemModelId' else 'fileAttributes'
                    root.find('.//' + Q(tag)).attrib.pop(attribute)
                result = link(supplier(remove))
                self.assertEqual(result['status'], 'metadata-unconfirmed')
                self.assertEqual(result['candidates'][0]['compatibility'], 'unknown')
        # Omitted model context validly falls back to the file context.
        p = supplier(lambda root: root.find('.//' + Q('representativeness')).attrib.pop('systemModelContextId'))
        self.assertEqual(link(p)['status'], 'matched')
        def unknown_model_context(root):
            root.find('.//' + Q('representativeness')).attrib.pop('systemModelContextId')
            root.find('.//' + Q('fileAttributes')).attrib.pop('contextId')
        self.assertEqual(link(supplier(unknown_model_context))['status'], 'metadata-unconfirmed')
        def no_model(root):
            modelling = root.find('.//' + Q('modellingAndValidation'))
            modelling.remove(modelling.find(Q('representativeness')))
        self.assertEqual(link(supplier(no_model))['status'], 'metadata-unconfirmed')
        request = self.modified(no_model)
        self.assertEqual(e.extract([request, DEMO / 'demo-electricity.spold'])['supplier-links'][0]['status'], 'metadata-unconfirmed')
        def different_revision_and_region(root):
            root.find('.//' + Q('fileAttributes')).set('majorRevision', '99')
            root.find('.//' + Q('fileAttributes')).set('minorRevision', '99')
            root.find('.//' + Q('geography')).set('geographyId', '00000000-0000-4000-8000-000000000098')
            root.find('.//' + Q('timePeriod')).set('startDate', '1999-01-01')
        revised = supplier(different_revision_and_region, 'revised.spold')
        self.assertEqual(link(revised)['status'], 'matched')
        result = e.extract([DEMO / 'demo-product.spold', DEMO / 'demo-electricity.spold', revised])['supplier-links'][0]
        self.assertEqual(result['status'], 'ambiguous')
        self.assertEqual(len(result['candidates']), 2)
        self.assertEqual(result['candidates'][1]['metadata']['dataset_revision']['major_revision'], '99')
        unknown = supplier(no_model, 'unknown.spold')
        result = e.extract([DEMO / 'demo-product.spold', DEMO / 'demo-electricity.spold', unknown])['supplier-links'][0]
        self.assertEqual(result['status'], 'metadata-unconfirmed')

    def test_lcia_values_and_stage(self):
        impact = self.result['impacts'][0]
        self.assertEqual(impact['amount'], '13.9')
        self.assertEqual(impact['normalized_amount'], '1.39')
        self.assertEqual(impact['unit_name'], 'kg CO2-eq')
        self.assertIsNone(impact['unit_id'])
        self.assertIsNone(impact['unit_context_id'])
        for k in ['impactMethodId', 'impactCategoryId', 'impactIndicatorId']:
            self.assertTrue(impact[k])
        result = e.extract([DEMO / 'demo-lcia.spold'], language='en', kind='lcia')
        self.assertEqual(result['impacts'][0]['name'], 'Teaching GWP (synthetic)')
        self.assertEqual(result['metadata'][0]['kind'], 'lcia')
        # Teaching arithmetic check, not a network calculation performed by extractor.
        self.assertEqual(Decimal('1.5') - Decimal('0.1') + Decimal('25') * Decimal('0.5'), Decimal('13.9'))

    def test_integer_groups_and_context_identity(self):
        for raw in ['  +0  ', '00', '-0']:
            p = self.modified(lambda root: setattr(root.find('.//' + Q('outputGroup')), 'text', raw))
            result = e.extract([p])
            self.assertEqual(result['exchanges'][0]['group'], raw)
            self.assertEqual(result['metadata'][0]['normalization']['status'], 'unique-positive-reference')
        p = self.modified(lambda root: setattr(root.find('.//' + Q('outputGroup')), 'text', '0_0'))
        with self.assertRaisesRegex(ValueError, 'XML integer'):
            e.extract([p])
        def explicit_contexts(root):
            ex = root.findall('.//' + Q('elementaryExchange'))[1]
            ex.set('elementaryExchangeContextId', '00000000-0000-4000-8000-000000000005')
            ex.set('unitContextId', '00000000-0000-4000-8000-000000000006')
            ex.find(Q('compartment')).set('subcompartmentContextId', '00000000-0000-4000-8000-000000000007')
        rows = e.extract([self.modified(explicit_contexts)])['exchanges']
        fossil = [x for x in rows if x['name'] == '二氧化碳，化石源（教学）']
        identity = lambda x: (x['flow_id'], x['flow_context_id'], x['subcompartment_id'], x['subcompartment_context_id'], x['unit_id'], x['unit_context_id'])
        self.assertEqual(len({identity(x) for x in fossil}), 2)

    def test_multilingual_missing_optional(self):
        self.assertEqual(len(self.product()[0]['names']), 2)
        en = e.extract([DEMO / 'demo-product.spold'], language='en')
        self.assertEqual(en['metadata'][0]['name'], 'Teaching product unit process')
        self.assertIsNone(en['exchanges'][0]['production_volume_amount'])
        self.assertIsNone(en['exchanges'][0]['xml_attributes'].get('sourceId'))
        def no_optional(root):
            m = root.find('.//' + Q('modellingAndValidation'))
            m.remove(m.find(Q('representativeness')))
            for ex in root.findall('.//' + Q('intermediateExchange')):
                for n in ['uncertainty', 'comment', 'synonym', 'tag']:
                    for child in ex.findall(Q(n)):
                        ex.remove(child)
        result = e.extract([self.modified(no_optional)])
        self.assertIsNone(result['metadata'][0]['system_model'])
        self.assertEqual(result['uncertainty'], [])

    def test_repeated_records_and_multiple_datasets(self):
        def duplicate(root):
            flow = root.find('.//' + Q('flowData'))
            ex = copy.deepcopy(flow.findall(Q('intermediateExchange'))[1])
            ex.set('id', '00000000-0000-4000-8000-000000000002')
            flow.insert(2, ex)
        result = e.extract([self.modified(duplicate)])
        self.assertEqual(len(result['exchanges']), 7)
        self.assertEqual(len(result['supplier-links']), 2)
        def multi(root):
            root.append(ET.parse(DEMO / 'demo-electricity.spold').getroot().find(Q('activityDataset')))
        result = e.extract([self.modified(multi)])
        self.assertEqual(len(result['metadata']), 2)
        self.assertEqual(result['supplier-links'][0]['status'], 'matched')

    def test_namespace_inheritance_and_uncertain_direction(self):
        p = self.modified(lambda root: setattr(root, 'tag', '{https://wrong.example/}ecoSpold'))
        with self.assertRaisesRegex(ValueError, 'namespace'):
            e.extract([p])
        p = self.modified(lambda root: setattr(root.find(Q('activityDataset')), 'tag', Q('childActivityDataset')))
        with self.assertRaisesRegex(ValueError, 'inheritance expansion'):
            e.extract([p])
        def no_group(root):
            ex = root.find('.//' + Q('intermediateExchange'))
            ex.remove(ex.find(Q('outputGroup')))
        with self.assertRaisesRegex(ValueError, 'direction'):
            e.extract([self.modified(no_group)])
        def wrong_flow_namespace(root):
            ex = root.find('.//' + Q('elementaryExchange'))
            ex.tag = '{https://wrong.example/}elementaryExchange'
        with self.assertRaisesRegex(ValueError, 'namespace'):
            e.extract([self.modified(wrong_flow_namespace)])
        def both(root):
            ET.SubElement(root.find('.//' + Q('intermediateExchange')), Q('inputGroup')).text = '1'
        with self.assertRaisesRegex(ValueError, 'direction'):
            e.extract([self.modified(both)])
        def duplicate(root):
            ET.SubElement(root.find('.//' + Q('intermediateExchange')), Q('outputGroup')).text = '0'
        with self.assertRaisesRegex(ValueError, 'duplicate singleton'):
            e.extract([self.modified(duplicate)])

    def test_unusable_references_and_missing_numbers(self):
        for raw, status in [('0', 'zero-reference'), ('-10', 'negative-reference')]:
            with self.subTest(raw=raw):
                p = self.modified(lambda root: root.find('.//' + Q('intermediateExchange')).set('amount', raw))
                result = e.extract([p])
                self.assertEqual(result['metadata'][0]['normalization']['status'], status)
                self.assertTrue(all(x['normalized_amount'] is None for x in result['exchanges']))
        def multi_ref(root):
            ex = root.findall('.//' + Q('intermediateExchange'))[1]
            ex.remove(ex.find(Q('inputGroup')))
            ET.SubElement(ex, Q('outputGroup')).text = '0'
        result = e.extract([self.modified(multi_ref)])
        self.assertEqual(result['metadata'][0]['normalization']['status'], 'multiple-references')
        self.assertTrue(all(x['normalized_amount'] is None for x in result['exchanges']))
        def missing(root):
            del root.find('.//' + Q('intermediateExchange')).attrib['amount']
        with self.assertRaisesRegex(ValueError, 'missing required attribute amount'):
            e.extract([self.modified(missing)])
        for raw in ['NaN', 'Infinity', '-Infinity', 'not-a-number', '1_0']:
            with self.subTest(raw=raw):
                with self.assertRaises(ValueError):
                    e.extract([self.modified(lambda root: root.find('.//' + Q('intermediateExchange')).set('amount', raw))])

    def test_formula_never_evaluated_and_cli(self):
        sentinel = self.dir / 'must-not-exist'
        formula = f"__import__('pathlib').Path({str(sentinel)!r}).touch()"
        p = self.modified(lambda root: root.findall('.//' + Q('intermediateExchange'))[1].set('mathematicalRelation', formula))
        result = e.extract([p])
        self.assertEqual(result['exchanges'][1]['xml_attributes']['mathematicalRelation'], formula)
        self.assertFalse(sentinel.exists())
        out = self.dir / 'out'
        call = subprocess.run([sys.executable, str(DEMO / 'extract_ecospold.py'), str(DEMO), '--out', str(out), '--language', 'en'], capture_output=True, text=True)
        self.assertEqual(call.returncode, 0, call.stderr)
        self.assertEqual({p.name for p in out.iterdir()}, {'metadata.json', 'exchanges.csv', 'parameters.csv', 'properties.csv', 'impacts.csv', 'uncertainty.json', 'supplier-links.json'})
        self.assertEqual(len(json.loads((out / 'metadata.json').read_text())), 3)


if __name__ == '__main__':
    unittest.main()

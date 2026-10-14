"""Check teaching fragments against original type declarations without altering XSD."""
from functools import lru_cache
from pathlib import Path
import copy
import json
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
NS_URI = 'http://www.EcoInvent.org/EcoSpold02'
SCHEMA_DIR = ROOT / 'content/ecospold2/original/Schemas'

class LocalResolver(etree.Resolver):
    def resolve(self, url, pubid, context):
        if Path(url).name == 'XmlNamespace.xsd':
            return self.resolve_filename(str(SCHEMA_DIR / 'XmlNamespace.xsd'),context)

@lru_cache(None)
def type_schema(sid):
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(LocalResolver())
    location = (SCHEMA_DIR / 'datasets/EcoSpold02.xsd').as_uri()
    wrapper = f'''<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
      xmlns:es="{NS_URI}" targetNamespace="{NS_URI}" elementFormDefault="qualified">
      <xs:include schemaLocation="{location}"/>
      <xs:element name="tutorialExample" type="es:{sid}"/>
    </xs:schema>'''
    return etree.XMLSchema(etree.fromstring(wrapper.encode(),parser))

def validate_fragment(sid, xml):
    node = etree.fromstring(xml.encode(),etree.XMLParser(no_network=True))
    if etree.QName(node).namespace != NS_URI:
        raise ValueError('Teaching fragment must use the original ecoSpold2 namespace')
    wrapped=copy.deepcopy(node)
    wrapped.tag = '{'+NS_URI+'}tutorialExample'
    type_schema(sid).assertValid(wrapped)
    return node

def field_nodes(node, field):
    path = '/'.join('es:'+p for p in field['schema']['nested'])
    parents = node.findall(path,{'es':NS_URI}) if path else [node]
    if field['name'].startswith('@'):
        return [p.attrib[field['name'][1:]] for p in parents if field['name'][1:] in p.attrib]
    return [n for p in parents for n in p.findall('es:'+field['name'],{'es':NS_URI})]

def validate_packets():
    source = json.loads((ROOT/'audit/ecospold2/source.json').read_text())
    sections = {}
    for suffix in 'abc':
        path = ROOT / f'audit/ecospold2/tutorial/xml-examples-{suffix}.json'
        if not path.exists():
            continue
        packet=json.loads(path.read_text())
        for sid,section in packet['sections'].items():
            if sid in sections:raise ValueError('Duplicate section '+sid)
            sections[sid]=section
    counts={}
    for official in source['sections']:
        sid=official['id']
        if sid not in sections:continue
        section=sections[sid]
        nodes=[validate_fragment(sid,e['xml']) for e in section['examples']]
        expected=[f['field_id'] for f in official['fields']]
        entries=[str(p['field_id']) for p in section['walkthrough']]
        if sorted(entries)!=sorted(expected):raise ValueError('Walkthrough coverage '+sid)
        for field in official['fields']:
            if not any(field_nodes(n,field) for n in nodes):
                raise ValueError('Field not shown in XML: '+sid+'/'+field['field_id'])
        counts[sid]=len(nodes)
    return counts

if __name__=='__main__':
    print(json.dumps(validate_packets(),ensure_ascii=False,indent=2))

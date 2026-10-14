"""Verify type validity, complete field coverage and published extraction examples."""
import importlib.util
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'content/ecospold2'
DEMO=BASE/'demo'
WORK=ROOT/'audit/ecospold2/tutorial'
sys.path.insert(0,str(ROOT/'tools'))
sys.path.insert(0,str(DEMO))
from ecospold_layout import CHAPTERS
from ecospold_xml_examples import validate_fragment, validate_packets, field_nodes
spec=importlib.util.spec_from_file_location('read_xml_fields',DEMO/'read_xml_fields.py')
reader=importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)

class XmlExampleTests(unittest.TestCase):
    def test_all_types_and_all_fields_appear_in_valid_fragments(self):
        counts=validate_packets()
        self.assertEqual(set(counts),set(CHAPTERS))
        source=json.loads((ROOT/'audit/ecospold2/source.json').read_text())
        manifest=json.loads((WORK/'manifest.json').read_text())
        records={r['section']:r for r in manifest['chapter_xml_examples']}
        self.assertEqual(set(records),set(CHAPTERS))
        fields=0
        for section in source['sections']:
            sid=section['id']
            fields+=len(section['fields'])
            entry=records[sid]
            self.assertEqual(len(entry['examples']),counts[sid])
            nodes=[validate_fragment(sid,(BASE/'xml-examples'/r['filename']).read_text()) for r in entry['examples']]
            for field in section['fields']:
                self.assertTrue(any(field_nodes(node,field) for node in nodes),(sid,field['field_id']))
                self.assertEqual(entry['field_paths'][field['field_id']],'/'.join(field['schema']['nested']+[field['name']]))
        self.assertEqual(fields,243)

    def test_every_inline_xml_and_runnable_field_code_matches_download(self):
        manifest=json.loads((WORK/'manifest.json').read_text())
        for section in manifest['chapter_xml_examples']:
            sid=section['section'];slug=CHAPTERS[sid][0]
            text=(BASE/(slug+'.md')).read_text()
            inline=re.findall(r'```xml\n(.*?)\n```',text,re.S)
            self.assertEqual(len(inline),len(section['examples']),sid)
            for xml,record in zip(inline,section['examples']):
                self.assertEqual(xml.strip(),(BASE/'xml-examples'/record['filename']).read_text().strip())
            template=next(c for c in re.findall(r'```python\n(.*?)\n```',text,re.S) if 'from read_xml_fields import' in c)
            for record in section['examples']:
                with self.subTest(section=sid,file=record['filename']):
                    code=template.replace('from read_xml_fields import field_values','field_values=reader.field_values')
                    code=code.replace('"xml-examples/'+slug+'-01.xml"',repr(str(BASE/'xml-examples'/record['filename'])))
                    printed=[]
                    env={'reader':reader,'print':lambda *args,**kwargs:printed.append(args)}
                    exec(compile(code,slug+'.md','exec'),env)
                    self.assertEqual(env['FIELDS'],section['field_paths'])
                    self.assertEqual(len(printed),len(section['field_paths']))
                    for fid,path,value in printed:
                        actual=json.loads(value)
                        node=validate_fragment(sid,(BASE/'xml-examples'/record['filename']).read_text())
                        # Independent XPath selection via lxml, not the reader implementation.
                        nested=path.split('/')
                        xpath='/'.join(p if p.startswith('@') else 'es:'+p for p in nested)
                        expected=node.xpath(xpath,namespaces={'es':reader.NS_URI})
                        if path.split('/')[-1].startswith('@'):
                            self.assertEqual(actual,[str(v) for v in expected])
                        else:
                            self.assertEqual([(r['attributes'],r['text']) for r in actual],[(dict(n.attrib),n.text) for n in expected])
                            for r,n in zip(actual,expected):
                                restored=ET.fromstring(r['xml'])
                                self.assertEqual(restored.tag,n.tag)
                                self.assertEqual(len(list(restored.iter())),len(list(n.iter())))

    def test_complete_spold_location_examples(self):
        from lxml import etree
        from read_section import NS
        manifest=json.loads((WORK/'manifest.json').read_text())
        for section in manifest['chapter_xml_examples']:
            sid=section['section'];slug=CHAPTERS[sid][0]
            text=(BASE/(slug+'.md')).read_text()
            code=next(c for c in re.findall(r'```python\n(.*?)\n```',text,re.S) if 'LOCATIONS =' in c)
            filename='demo-lcia.spold' if sid=='TImpactIndicatorResult' else 'demo-product.spold'
            code=code.replace('"'+filename+'"',repr(str(DEMO/filename)))
            printed=[]
            env={'FIELDS':section['field_paths'],'field_values':reader.field_values,
                 'json':json,'print':lambda *args,**kwargs:printed.append(args)}
            exec(compile(code,slug+'.md','exec'),env)
            ds=etree.parse(str(DEMO/filename)).find('es:activityDataset',NS)
            expected=[]
            for location in env['LOCATIONS']:
                nodes=ds.xpath(location,namespaces=NS)
                expected.append(('父路径：',location,'匹配数：',len(nodes)))
                for node in nodes:
                    for fid,path in section['field_paths'].items():
                        xpath='/'.join(p if p.startswith('@') else 'es:'+p for p in path.split('/'))
                        values=node.xpath(xpath,namespaces=NS)
                        expected.append((fid,path,values))
            self.assertEqual(len(printed),len(expected),sid)
            for actual,wanted in zip(printed,expected):
                if len(wanted)==4:
                    self.assertEqual(actual,wanted)
                else:
                    self.assertEqual(actual[:2],wanted[:2])
                    values=json.loads(actual[2])
                    if wanted[1].split('/')[-1].startswith('@'):
                        self.assertEqual(values,[str(v) for v in wanted[2]])
                    else:
                        self.assertEqual([(v['attributes'],v['text']) for v in values],[(dict(n.attrib),n.text) for n in wanted[2]])

    def test_absence_multilingual_nested_and_formula_are_raw(self):
        root=ET.fromstring('''<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02" amount="-0.1" mathematicalRelation="do_not_execute()"><normal variance="0"/><comment xml:lang="zh">教学</comment><comment xml:lang="en">teaching</comment></uncertainty>''')
        self.assertEqual(reader.field_values(root,'@amount'),['-0.1'])
        self.assertEqual(reader.field_values(root,'lognormal/@variance'),[])
        self.assertEqual(reader.field_values(root,'normal/@variance'),['0'])
        self.assertEqual(reader.field_values(root,'@mathematicalRelation'),['do_not_execute()'])
        comments=reader.field_values(root,'comment')
        self.assertEqual([r['text'] for r in comments],['教学','teaching'])
        self.assertEqual([r['attributes']['{http://www.w3.org/XML/1998/namespace}lang'] for r in comments],['zh','en'])
        self.assertEqual(reader.field_values(root,'@missing'),[])
        with self.assertRaises(ValueError):reader.field_values(ET.Element('uncertainty'),'@amount')

if __name__=='__main__':
    unittest.main(verbosity=2)

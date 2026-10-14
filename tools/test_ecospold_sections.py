"""Verify raw narrative-section reading and the 22 published runnable examples."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / 'content/ecospold2/demo'
sys.path.insert(0,str(ROOT / 'tools'))
from ecospold_layout import CHAPTERS
spec = importlib.util.spec_from_file_location('read_section', DEMO / 'read_section.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class SectionReadingTests(unittest.TestCase):
    def test_published_examples_and_excerpt_match_actual_file(self):
        source = json.loads((ROOT / 'audit/ecospold2/source.json').read_text())
        self.assertEqual(set(m.PATHS),{s['id'] for s in source['sections']})
        for sid,(slug,title) in CHAPTERS.items():
            with self.subTest(section=sid):
                text = (DEMO.parent / (slug+'.md')).read_text()
                code = next(c for c in re.findall(r'```python\n(.*?)\n```',text,re.S) if 'from read_section import' in c and 'records = read_section' in c)
                filename = re.search(r'load_dataset\("([^"]+)"',code).group(1)
                code = code.replace('from read_section import load_dataset, read_section','load_dataset = reader.load_dataset\nread_section = reader.read_section')
                code = code.replace('"'+filename+'"',repr(str(DEMO / filename)))
                output = []
                env = {'reader':m,'print':lambda *args,**kwargs: output.append(args)}
                exec(compile(code,slug+'.md','exec'),env)
                records = env['records']
                self.assertEqual(records,m.read_section(m.load_dataset(DEMO / filename),sid))
                self.assertEqual(output[0],('匹配节点数：',len(records)))
                self.assertEqual(json.loads(output[1][0]),records[:2])
                if records:
                    first = records[0]
                    expected={'path':first['path'],'attributes':first['attributes'],
                              'children_excerpt':[{'tag':n['tag'],'attributes':n['attributes'],'text':n['text']} for n in first['children'][:2]]}
                    self.assertEqual(json.loads(re.search(r'```json\n(.*?)\n```',text,re.S).group(1)),expected)
                else:
                    self.assertIn('返回空列表',text)

    def test_parent_paths_signs_nested_amounts_and_language_survive(self):
        ds = m.load_dataset(DEMO/'demo-product.spold')
        rows=m.read_section(ds,'TCustomExchange')
        self.assertEqual(len(rows),6)
        self.assertTrue(any(r['attributes']['amount']=='-0.1' and any(c['tag'].endswith('outputGroup') for c in r['children']) for r in rows))
        reference = next(r for r in rows if r['attributes']['amount']=='10')
        prop = next(c for c in reference['children'] if c['tag'].endswith('property'))
        self.assertEqual(prop['attributes']['amount'],'1')
        names = [c for c in reference['children'] if c['tag'].endswith('name')]
        self.assertEqual([c['attributes']['{http://www.w3.org/XML/1998/namespace}lang'] for c in names],['zh','en'])
        self.assertEqual(len(set(r['path'] for r in rows)),len(rows))
        self.assertEqual(len(m.read_section(ds,'TUncertainty')),1)
        text_nodes = m.read_section(ds,'TTextAndImage')
        self.assertTrue(any(r['path'].endswith('generalComment[1]') for r in text_nodes))
        self.assertFalse(any('/parameter[' in r['path'] for r in text_nodes))

    def test_activity_and_product_classification_keep_distinct_parents(self):
        ds=m.load_dataset(DEMO/'demo-product.spold')
        activity_class=ET.fromstring('<classification xmlns="'+m.NS_URI+'" classificationId="00000000-0000-4000-8000-000000000001"><classificationSystem>test</classificationSystem><classificationValue>activity-specific-classification</classificationValue></classification>')
        ds.find('es:activityDescription',m.NS).append(activity_class)
        product=ds.find('es:flowData/es:intermediateExchange',m.NS)
        copied=copy.deepcopy(activity_class)
        copied.find('es:classificationValue',m.NS).text='product-specific-classification'
        product.append(copied)
        rows=m.read_section(ds,'TClassification')
        self.assertEqual(len(rows),2)
        self.assertTrue(rows[0]['path'].startswith('/ecoSpold/activityDataset/activityDescription'))
        self.assertTrue(rows[1]['path'].startswith('/ecoSpold/activityDataset/flowData'))
        self.assertTrue(any(c['text']=='product-specific-classification' for c in rows[1]['children']))

    def test_optional_absence_multi_dataset_and_child_rejection(self):
        root=ET.parse(DEMO/'demo-product.spold').getroot()
        self.assertEqual(m.read_section(root[0],'TTransferCoefficient'),[])
        second=copy.deepcopy(root[0]);second.find('es:activityDescription/es:activity',m.NS).set('id','second-activity')
        root.append(second)
        with tempfile.TemporaryDirectory() as tmp:
            file=Path(tmp)/'multi.spold'
            ET.ElementTree(root).write(file)
            self.assertEqual(m.read_section(m.load_dataset(file,1),'TActivity')[0]['attributes']['id'],'second-activity')
            with self.assertRaises(IndexError): m.load_dataset(file,2)
            ET.SubElement(root,'{'+m.NS_URI+'}childActivityDataset')
            ET.ElementTree(root).write(file)
            with self.assertRaisesRegex(ValueError,'inheritance'):m.load_dataset(file)
        with self.assertRaises(KeyError):m.read_section(root[0],'Unknown')
        with self.assertRaises(ValueError):m.read_section(ET.Element('activityDataset'),'TActivity')

if __name__ == '__main__':
    unittest.main(verbosity=2)

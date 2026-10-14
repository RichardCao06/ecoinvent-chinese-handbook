"""Read raw fields from a namespace-qualified teaching XML fragment or real node."""
import xml.etree.ElementTree as ET

NS_URI = 'http://www.EcoInvent.org/EcoSpold02'
NS = {'es':NS_URI}

def field_values(node, path):
    """Return all actual values, [] for absence, with no defaults or evaluation.

    A path is relative to the selected node, e.g. @amount, unitName,
    lognormal/@variance. Element records retain attributes and complete XML.
    """
    if not node.tag.startswith('{'+NS_URI+'}'):
        raise ValueError('Expected an ecoSpold2 namespace-qualified element')
    parts=path.split('/')
    if not parts or any(not p or p in ('.','..') for p in parts):
        raise ValueError('Expected a relative field path')
    parents=[node]
    for part in parts[:-1]:
        if part.startswith('@'):
            raise ValueError('Attributes can only terminate a field path')
        parents=[child for parent in parents for child in parent.findall('es:'+part,NS)]
    last=parts[-1]
    if last.startswith('@'):
        name=last[1:]
        return [parent.attrib[name] for parent in parents if name in parent.attrib]
    return [{'attributes':dict(child.attrib),'text':child.text,
             'xml':ET.tostring(child,encoding='unicode')}
            for parent in parents for child in parent.findall('es:'+last,NS)]

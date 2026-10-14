"""Read raw section nodes; synthetic tutorial helper, not an LCA calculation."""
import xml.etree.ElementTree as ET

NS_URI = 'http://www.EcoInvent.org/EcoSpold02'
NS = {'es': NS_URI}
PATHS = {
    'TActivity': ['activityDescription/activity'],
    'TClassification': ['activityDescription/classification', 'flowData/intermediateExchange/classification'],
    'TGeography': ['activityDescription/geography'],
    'TTechnology': ['activityDescription/technology'],
    'TTimePeriod': ['activityDescription/timePeriod'],
    'TMacroEconomicScenario': ['activityDescription/macroEconomicScenario'],
    'TCustomExchange': ['flowData/intermediateExchange', 'flowData/elementaryExchange'],
    'TIntermediateExchange': ['flowData/intermediateExchange'],
    'TElementaryExchange': ['flowData/elementaryExchange'],
    'TParameter': ['flowData/parameter'],
    'TImpactIndicatorResult': ['flowData/impactIndicator'],
    'TCompartment': ['flowData/elementaryExchange/compartment'],
    'TUncertainty': ['.//uncertainty', './/productionVolumeUncertainty'],
    'TProperty': ['flowData/intermediateExchange/property', 'flowData/elementaryExchange/property'],
    'TTransferCoefficient': ['flowData/intermediateExchange/transferCoefficient', 'flowData/elementaryExchange/transferCoefficient'],
    'TTextAndImage': ['activityDescription/activity/generalComment',
                      'activityDescription/activity/allocationComment',
                      'activityDescription/geography/comment', 'activityDescription/technology/comment',
                      'activityDescription/timePeriod/comment', 'modellingAndValidation/review/details'],
    'TRepresentativeness': ['modellingAndValidation/representativeness'],
    'TReview': ['modellingAndValidation/review'],
    'TDataEntryBy': ['administrativeInformation/dataEntryBy'],
    'TDataGeneratorAndPublication': ['administrativeInformation/dataGeneratorAndPublication'],
    'TFileAttributes': ['administrativeInformation/fileAttributes'],
    'TRequiredContextReference': ['administrativeInformation/fileAttributes/requiredContext'],
}


def load_dataset(filename, index=0):
    """Select a complete dataset explicitly; do not silently read a child delta."""
    root = ET.parse(filename).getroot()
    if root.tag != '{' + NS_URI + '}ecoSpold':
        raise ValueError('Expected ecoSpold2 namespace and ecoSpold root')
    if root.find('es:childActivityDataset', NS) is not None:
        raise ValueError('Resolve child dataset inheritance before reading')
    datasets = root.findall('es:activityDataset', NS)
    if not 0 <= index < len(datasets):
        raise IndexError('Dataset index is outside the file')
    return datasets[index]


def node_record(node, path):
    """Keep original attribute strings, namespace-qualified names and child order."""
    counts = {}
    children = []
    for child in node:
        local = child.tag.split('}')[-1]
        counts[local] = counts.get(local, 0) + 1
        children.append(node_record(child, f'{path}/{local}[{counts[local]}]'))
    return {'path': path, 'tag': node.tag, 'attributes': dict(node.attrib),
            'text': node.text, 'children': children}


def read_section(dataset, section):
    """Return all matching nodes with their parent paths; absence remains []."""
    if dataset.tag != '{' + NS_URI + '}activityDataset':
        raise ValueError('Expected complete activityDataset in ecoSpold2 namespace')
    if section not in PATHS:
        raise KeyError('Unknown section: ' + section)
    wanted = {id(n) for path in PATHS[section]
              for n in dataset.findall('/'.join('es:' + p if p not in ('.', '') else p
                                               for p in path.split('/')), NS)}
    found = []

    def visit(node, path):
        if id(node) in wanted:
            found.append(node_record(node, path))
        counts = {}
        for child in node:
            local = child.tag.split('}')[-1]
            counts[local] = counts.get(local, 0) + 1
            visit(child, f'{path}/{local}[{counts[local]}]')

    visit(dataset, '/ecoSpold/activityDataset')
    return found

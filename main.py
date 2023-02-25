import pydot
from xml.etree import ElementTree


def parse_bpmn_file(filename):
    """
    Cette fonction parse le fichier BPMN et retourne une liste des éléments contenus dans le fichier
    """
    bpmn_elements = []
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == '{http://www.omg.org/spec/BPMN/20100524/MODEL%7Dprocess':
            for process_elements in child:
                element_info = {'type': process_elements.tag.split('}')[-1],
                                'name': process_elements.attrib.get('name', ''),
                                'outgoing': process_elements.attrib.get('outgoing', '')}
                bpmn_elements.append(element_info)
    return bpmn_elements


def bpmn_to_petri(bpmn_diagram):
    places = {}
    petri_net = {'places': [], 'transitions': [], 'arcs': []}
    for element in bpmn_diagram:
        if element['type'] == 'startEvent':
            transition_name = 'start'
            if element['name'] not in places:
                places[element['name']] = len(petri_net['places']) + 1
                petri_net['places'].append(element['name'])
            petri_net['arcs'].append((transition_name, places[element['name']]))
        elif element['type'] == 'endEvent':
            transition_name = 'end'
            if element['name'] not in places:
                places[element['name']] = len(petri_net['places']) + 1
                petri_net['places'].append(element['name'])
            petri_net['arcs'].append((places[element['name']], transition_name))
        elif element['type'] == 'task':
            transition_name = element['name']
            if element['name'] not in places:
                places[element['name']] = len(petri_net['places']) + 1
                petri_net['places'].append(element['name'])
            petri_net['transitions'].append(transition_name)
            for outgoing in element['outgoing'].split():
                if outgoing.split(':')[-1] not in places:
                    places[outgoing.split(':')[-1]] = len(petri_net['places']) + 1
                    petri_net['places'].append(outgoing.split(':')[-1])
                petri_net['arcs'].append((transition_name, places[outgoing.split(':')[-1]]))
    return petri_net


def petri_net_to_graph(petri_net, filename):
    """
    Cette fonction crée un graphique du réseau de Petri à partir des données
    """
    graph = pydot.Dot(rankdir='LR', margin=0.1)
    for place in petri_net['places']:
        graph.add_node(pydot.Node(place, shape='circle'))
    for transition in petri_net['transitions']:
        graph.add_node(pydot.Node(transition, shape='box'))
    for arc in petri_net['arcs']:
        graph.add_edge(pydot.Edge(arc[0], arc[1]))
    graph.write(path=filename, format="png")


if __name__ == '__main__':
    # Lire le fichier BPMN
    bpmn_diagram = parse_bpmn_file('pizza-collaboration.bpmn')
    # Convertir en réseau de Petri
    petri_net = bpmn_to_petri(bpmn_diagram)
    # Créer un graphique du réseau de Petri
    petri_net_to_graph(petri_net, 'petri_net.png')

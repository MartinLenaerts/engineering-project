import pydot

from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.event_based_gateway import EventBasedGateway
from classes.PETRI.arc import Arc
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition
from utils.bpmn_functions import parse_bpmn_file


def translate_bpmn_element(element, petri_net, place_id=0, already_translated=None):
    if already_translated is None:
        already_translated = []

    petri_element = None
    for (e, e_id) in already_translated:
        if e_id == element.element_id:
            return e

    if isinstance(element, StartEvent):
        place = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        transition = Transition(element.name)
        petri_net.add_transition(transition)

        arc = Arc(place, transition)
        petri_net.add_arc(arc)

        target = translate_bpmn_element(element.outgoing_elements[0], petri_net, place_id, already_translated)

        if target is None:
            target = Place("None Place ! target of {}".format(element.element_id), 0)

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if isinstance(element, EndEvent):
        placeEnd = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(placeEnd)

        transition = Transition(element.name)
        petri_net.add_transition(transition)

        arc = Arc(transition, placeEnd)
        petri_net.add_arc(arc)

        place = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        arc = Arc(place, transition)
        petri_net.add_arc(arc)

        petri_element = place

    if isinstance(element, SequenceFlow):
        petri_element = translate_bpmn_element(element.target, petri_net, place_id, already_translated)

    if isinstance(element, Task):
        place = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        transition = Transition(element.name)
        petri_net.add_transition(transition)
        petri_element = place

        arc = Arc(place, transition)

        petri_net.add_arc(arc)

        target = translate_bpmn_element(element.outgoing_elements[0], petri_net, place_id, already_translated)

        if target is None:
            target = Place("None Place ! target of {}".format(element.element_id), 0)

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if isinstance(element, EventBasedGateway):
        place = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)
        petri_element = place

        for out_element in element.outgoing_elements:
            target = translate_bpmn_element(out_element, petri_net, place_id, already_translated)

            if target is None:
                target = Place("None Place ! target of {}".format(element.element_id), 0)

            arc = Arc(place, target)
            petri_net.add_arc(arc)

    if isinstance(element, IntermediateEvent):
        place = Place("p{}".format(place_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        transition = Transition(element.name)
        petri_net.add_transition(transition)
        petri_element = place

        arc = Arc(place, transition)

        petri_net.add_arc(arc)

        target = translate_bpmn_element(element.outgoing_elements[0], petri_net, place_id, already_translated)

        if target is None:
            target = Place("None Place ! target of {}".format(element.element_id), 0)

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if petri_element is None:
        print(element.__class__.__name__)

    already_translated.append((petri_element, element.element_id))

    return petri_element


def bpmn_to_petri(bpmn):
    elements = bpmn.get_start_event()
    petri_net = PetriNet()

    translate_bpmn_element(elements[0], petri_net)

    print(petri_net)

    petri_net_to_graph(petri_net, "temp.png")


def petri_net_to_graph(petri_net, filename):
    graph = pydot.Dot(rankdir='LR', margin=0.1)
    for place in petri_net.places:
        graph.add_node(pydot.Node(place.name, shape='circle'))
    for transition in petri_net.transitions:
        graph.add_node(pydot.Node(transition.name, shape='box'))
    for arc in petri_net.arcs:
        graph.add_edge(pydot.Edge(arc.source.name, arc.target.name))
    graph.write(path=filename, format="png")


if __name__ == '__main__':
    bpmn_diagram = parse_bpmn_file('docs/bpmn/pizza-collaboration-light.bpmn')

    print(bpmn_diagram)

    bpmn_to_petri(bpmn_diagram)

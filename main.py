import os
import time

import pydot

from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.gateway import Gateway
from classes.PETRI.arc import Arc
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition
from utils.bpmn_functions import parse_bpmn_file


def translate_bpmn_element(element, petri_net, place_id, already_translated):
    petri_element = None

    for (petri_element, bpmn_element) in already_translated:
        if bpmn_element.element_id == element.element_id:
            return petri_element

    if isinstance(element, StartEvent):
        place = None
        for (_, e) in already_translated:
            if isinstance(e, StartEvent):
                for p in petri_net.places:
                    if p.id == e.element_id:
                        place = p

        if place is None:
            place = Place("p{}".format(element.element_id), element.element_id)
            already_translated.append((place, element))
            place_id += 1
            petri_net.add_place(place)

        transition = Transition(element.name)
        petri_net.add_transition(transition)

        arc = Arc(place, transition)
        petri_net.add_arc(arc)

        target = translate_bpmn_element(element.outgoing_elements[0],
                                        petri_net,
                                        place_id,
                                        already_translated
                                        )

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if isinstance(element, EndEvent):
        place_end = Place("p{}".format(element.element_id), element.element_id)
        place_id += 1
        petri_net.add_place(place_end)

        transition = Transition(element.name)
        petri_net.add_transition(transition)

        arc = Arc(transition, place_end)
        petri_net.add_arc(arc)

        place = Place("p{}".format(element.element_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        arc = Arc(place, transition)
        petri_net.add_arc(arc)

        petri_element = place
        already_translated.append((petri_element, element))

    if isinstance(element, SequenceFlow):
        petri_element = translate_bpmn_element(element.target, petri_net, place_id, already_translated)

    if isinstance(element, Task) or isinstance(element, IntermediateEvent):
        place = Place("p{}".format(element.element_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)

        transition = Transition(element.name)
        petri_net.add_transition(transition)
        petri_element = place
        already_translated.append((petri_element, element))

        arc = Arc(place, transition)

        petri_net.add_arc(arc)

        target = translate_bpmn_element(element.outgoing_elements[0], petri_net, place_id, already_translated)

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if isinstance(element, Gateway):
        place = Place("p{}".format(element.element_id), element.element_id)
        place_id += 1
        petri_net.add_place(place)
        petri_element = place
        already_translated.append((petri_element, element))

        for out_element in element.outgoing_elements:
            target = translate_bpmn_element(out_element, petri_net, place_id, already_translated)

            arc = Arc(place, target)
            petri_net.add_arc(arc)

    return petri_element


def bpmn_to_petri(bpmn, filename):
    elements = bpmn.get_start_event()
    petri_net = PetriNet()
    already_translated = []
    place_id = 0

    for start in elements:
        translate_bpmn_element(start, petri_net, place_id, already_translated)

    place_id = 0
    for place in petri_net.places:
        place.name = "p{}".format(place_id)
        place_id += 1

    petri_net_to_graph(petri_net, "{}.png".format(filename))


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
    dir_path = 'docs/bpmn/'

    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isfile(path):
            bpmn_diagram = parse_bpmn_file(path)

            bpmn_to_petri(bpmn_diagram, 'docs/petri/{}'.format(file.replace('.bpmn', '')))

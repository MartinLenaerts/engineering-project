from classes.BPMN.connecting.message_flow import MessageFlow
from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.gateway import Gateway
from classes.BPMN.flow.sub_process import SubProcess
from classes.PETRI.arc import Arc
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition


def create_place_and_transition(bpmn_element, petri_net):
    place = Place("p{}".format(bpmn_element.element_id), bpmn_element.element_id)
    transition = Transition(bpmn_element.name, bpmn_element.element_id)
    arc = Arc(place, transition)

    petri_net.add_place(place)
    petri_net.add_transition(transition)
    petri_net.add_arc(arc)

    return place, transition


def translate_bpmn_element(element, petri_net, already_translated):
    petri_element = None

    for (petri_element, bpmn_element) in already_translated:
        if bpmn_element.element_id == element.element_id:
            return petri_element

    if isinstance(element, StartEvent):
        place, transition = create_place_and_transition(element, petri_net)

        already_translated.append((place, element))

        target = translate_bpmn_element(element.outgoing_elements[0],
                                        petri_net,
                                        already_translated
                                        )

        arc = Arc(transition, target)
        petri_net.add_arc(arc)

    if isinstance(element, EndEvent):
        place, transition = create_place_and_transition(element, petri_net)
        petri_element = place

        place_end = Place("p{}".format(element.element_id), element.element_id)
        petri_net.add_place(place_end)

        arc = Arc(transition, place_end)
        petri_net.add_arc(arc)

        already_translated.append((place, element))

    if isinstance(element, SequenceFlow) or isinstance(element, MessageFlow):
        petri_element = translate_bpmn_element(element.target, petri_net, already_translated)

    if isinstance(element, Task) or isinstance(element, IntermediateEvent) or isinstance(element, SubProcess):

        place, transition = create_place_and_transition(element, petri_net)
        already_translated.append((place, element))

        petri_element = place

        for e in element.outgoing_elements:
            target = translate_bpmn_element(e, petri_net, already_translated)
            arc = Arc(transition, target)
            petri_net.add_arc(arc)

    if isinstance(element, Gateway):
        #for in_element in element.incoming_elements:
        place = Place("p{}".format(element.element_id), element.element_id)

        petri_net.add_place(place)
        petri_element = place
        already_translated.append((petri_element, element))

        for out_element in element.outgoing_elements:
            transition = Transition(element.name, element.element_id)
            petri_net.add_place(transition)
            arc = Arc(place, transition)
            petri_net.add_arc(arc)

            target = translate_bpmn_element(out_element, petri_net, already_translated)

            arc = Arc(transition, target)
            petri_net.add_arc(arc)

    return petri_element


def bpmn_to_petri(bpmn):
    elements = bpmn.get_start_event()
    petri_net = PetriNet()
    already_translated = []

    for start in elements:
        translate_bpmn_element(start, petri_net, already_translated)

    place_id = 0
    for place in petri_net.places:
        place.name = "p{}".format(place_id)
        place_id += 1

    return petri_net

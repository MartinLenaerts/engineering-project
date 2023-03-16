from classes.BPMN.connecting.message_flow import MessageFlow
from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.exclusive_gateway import ExclusiveGateway
from classes.BPMN.flow.gateway.parallel_gateway import ParallelGateway
from classes.BPMN.flow.sub_process import SubProcess
from classes.PETRI.arc import Arc
from classes.PETRI.petri_element import PetriElement
from classes.PETRI.petri_net import PetriNet
from classes.PETRI.place import Place
from classes.PETRI.transition import Transition


def create_place_and_transition(bpmn_element, petri_net):
    place = Place("p{}".format(bpmn_element.element_id), bpmn_element.element_id, petri_net)
    transition = Transition(bpmn_element.name, bpmn_element.element_id, petri_net)
    Arc(place, transition, petri_net)

    return place, transition


def translate_bpmn_element(element, petri_net, already_translated, source=None):
    petri_element = None

    for (petri_elements, bpmn_element) in already_translated:
        if bpmn_element.element_id == element.element_id:
            if isinstance(petri_elements, PetriElement):
                return petri_elements
            elif source is not None:
                for petri_element in petri_elements:
                    if petri_element.id == source["element_id"]:
                        return petri_element

    if isinstance(element, StartEvent):
        place, transition = create_place_and_transition(element, petri_net)

        already_translated.append((place, element))

        target = translate_bpmn_element(element.outgoing_elements[0],
                                        petri_net,
                                        already_translated,
                                        {"element_id": element.element_id})

        Arc(transition, target, petri_net)

    if isinstance(element, EndEvent):
        place, transition = create_place_and_transition(element, petri_net)
        petri_element = place

        place_end = Place("p{}".format(element.element_id), element.element_id, petri_net)
        Arc(transition, place_end, petri_net)

        already_translated.append((place, element))

    if isinstance(element, SequenceFlow) or isinstance(element, MessageFlow):
        petri_element = translate_bpmn_element(element.target, petri_net, already_translated,
                                               {"element_id": element.element_id})
    if isinstance(element, Task) or isinstance(element, IntermediateEvent) or \
            isinstance(element, SubProcess) or isinstance(element, ParallelGateway):

        if isinstance(element, SubProcess):
            transition = Transition(element.name, element.element_id, petri_net, "yellow")
            sub_petri_net = PetriNet()
            sub_already_translated = []
            for sub_element in element.get_start_event():
                translate_bpmn_element(sub_element, sub_petri_net, sub_already_translated)

            petri_net.add_sub_net(sub_petri_net)
        else:
            transition = Transition(element.name, element.element_id, petri_net)
        petri_elements = []

        for in_element in element.incoming_elements:
            place = Place("p{}".format(in_element.element_id), in_element.element_id, petri_net)

            if source["element_id"] == in_element.element_id:
                petri_element = place

            petri_elements.append(place)
            Arc(place, transition, petri_net)

        already_translated.append((petri_elements, element))

        for out_element in element.outgoing_elements:
            target = translate_bpmn_element(out_element, petri_net, already_translated,
                                            {"element_id": element.element_id})
            Arc(transition, target, petri_net)

    if isinstance(element, ExclusiveGateway):
        more_entry = len(element.incoming_elements) > len(element.outgoing_elements)

        if more_entry:
            out_place = translate_bpmn_element(element.outgoing_elements[0], petri_net, already_translated,
                                               {"element_id": element.element_id})

            petri_elements = []
            for in_element in element.incoming_elements:
                place = Place("p{}".format(in_element.element_id), in_element.element_id, petri_net)

                if source["element_id"] == in_element.element_id:
                    petri_element = place

                petri_elements.append(place)

                transition = Transition(in_element.name, in_element.element_id, petri_net)

                Arc(place, transition, petri_net)

                Arc(transition, out_place, petri_net)
            already_translated.append((petri_elements, element))
        else:
            place = Place("p{}".format(element.element_id), element.element_id, petri_net)
            petri_element = place
            already_translated.append((place, element))

            for out_element in element.outgoing_elements:
                transition = Transition(out_element.name, out_element.element_id, petri_net)
                Arc(place, transition, petri_net)

                target = translate_bpmn_element(out_element, petri_net, already_translated,
                                                {"element_id": element.element_id})

                Arc(transition, target, petri_net)

    return petri_element


def bpmn_to_petri(bpmn):
    elements = bpmn.get_start_event()
    petri_net = PetriNet()
    already_translated = []

    for start in elements:
        translate_bpmn_element(start, petri_net, already_translated)

    place_id = 0
    for place in petri_net.get_all_places():
        place.name = "{}".format(place_id)
        place_id += 1

    return petri_net

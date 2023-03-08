from xml.etree import ElementTree

from classes.BPMN.bpmn_diagram import BpmnDiagram
from classes.BPMN.connecting.message_flow import MessageFlow
from classes.BPMN.connecting.sequence_flow import SequenceFlow
from classes.BPMN.flow.activity.task import Task
from classes.BPMN.flow.event.end_event import EndEvent
from classes.BPMN.flow.event.intermediate_event import IntermediateEvent
from classes.BPMN.flow.event.start_event import StartEvent
from classes.BPMN.flow.gateway.event_based_gateway import EventBasedGateway
from classes.BPMN.flow.gateway.parallel_gateway import ParallelGateway

from classes.BPMN.lane import Lane
from classes.BPMN.process import Process
from classes.BPMN.flow.sub_process import SubProcess
from constant.bpmn_xml_elements import BpmnXmlElement
from utils.functions import get_name


def add_element_to_process(element, process):
    append = False
    if hasattr(process, "lanes"):
        for lane in process.lanes:
            for e_id in lane.elements_ids:
                if e_id == element.element_id and append is False:
                    lane.append_element(element)
                    append = True

    if append is False:
        process.append_element(element)


def find_source_and_target(xml_child, bpmn_diagram):
    source_ref = xml_child.attrib.get('sourceRef')
    target_ref = xml_child.attrib.get('targetRef')
    target_found = False
    source_found = False
    target = None
    source = None
    if hasattr(bpmn_diagram, "processes"):
        for process in bpmn_diagram.processes:
            for lane in process.lanes:
                for element in lane.elements:
                    if element.element_id == source_ref:
                        source = element
                        source_found = True
                    if element.element_id == target_ref:
                        target = element
                        target_found = True

            if target_found is False or source_found is False:
                for element in process.elements:
                    if element.element_id == source_ref:
                        source = element
                    if element.element_id == target_ref:
                        target = element
    else:
        for element in bpmn_diagram.elements:
            if element.element_id == source_ref:
                source = element
            if element.element_id == target_ref:
                target = element

    return source, target


def map_elements_of_process(process_xml, process, bpmn_diagram):
    for xml_child in process_xml:
        element = None
        if xml_child.tag == BpmnXmlElement.START_EVENT.value:
            element = StartEvent(xml_child)
        if xml_child.tag == BpmnXmlElement.END_EVENT.value:
            element = EndEvent(xml_child)
        if xml_child.tag == BpmnXmlElement.PARALLEL_GATEWAY.value:
            element = ParallelGateway(xml_child)
        if xml_child.tag == BpmnXmlElement.EXCLUSIVE_GATEWAY.value:
            element = ParallelGateway(xml_child)
        if xml_child.tag == BpmnXmlElement.EVENT_BASED_GATEWAY.value:
            element = EventBasedGateway(xml_child)
        if xml_child.tag == BpmnXmlElement.INTERMEDIATE_CATCH_EVENT.value:
            element = IntermediateEvent(xml_child)
        if xml_child.tag == BpmnXmlElement.TASK.value:
            element = Task(xml_child, xml_child.attrib.get('startQuantity'))
        if xml_child.tag == BpmnXmlElement.SUB_PROCESS.value:
            element = SubProcess(xml_child)
            map_elements_of_process(xml_child, element, element)

        if element is not None:
            add_element_to_process(element, process)
        elif xml_child.tag != BpmnXmlElement.SEQUENCE_FLOW.value:
            print("⚠️ '{}' tag not found !".format(xml_child.tag))

    sequences = process_xml.findall(BpmnXmlElement.SEQUENCE_FLOW.value)
    for xml_sequence in sequences:
        source, target = find_source_and_target(xml_sequence, bpmn_diagram)
        flow = SequenceFlow(xml_sequence, source, target, 0)
        process.append_element(flow)

def create_bpmn_diagram(xml):
    bpmn_diagram = BpmnDiagram()

    processes = xml.findall(BpmnXmlElement.PROCESS.value)
    for process_xml in processes:
        process = Process(process_xml)
        bpmn_diagram.append_process(process)
        lane_set_xml = process_xml.find(BpmnXmlElement.LANE_SET.value)

        if lane_set_xml is not None:
            for lane_xml in lane_set_xml:
                ids = []
                for child in lane_xml:
                    ids.append(child.text)

                lane = Lane(lane_xml, ids)
                process.append_lane(lane)

        map_elements_of_process(process_xml, process, bpmn_diagram)

    collaboration = xml.find(BpmnXmlElement.COLLABORATION.value)
    if collaboration is not None:
        for xml_child in collaboration:
            if xml_child.tag == BpmnXmlElement.MESSAGE_FLOW.value:
                source, target = find_source_and_target(xml_child, bpmn_diagram)

                message_flow = MessageFlow(xml_child, source, target)
                bpmn_diagram.append_element(message_flow)

            if xml_child.tag == BpmnXmlElement.PARTICIPANT.value:
                for process in bpmn_diagram.processes:
                    if process.process_id == xml_child.attrib.get('processRef'):
                        process.name = get_name(xml_child)

    return bpmn_diagram


def parse_bpmn_file(filename):
    tree = ElementTree.parse(filename)
    root = tree.getroot()

    return create_bpmn_diagram(root)

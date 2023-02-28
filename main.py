import pydot
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
from constant.bpmn_xml_elements import BpmnXmlElement
from utils.functions import get_name, get_id


def parse_bpmn_file(filename):
    """
    Cette fonction parse le fichier BPMN et retourne une liste des éléments contenus dans le fichier
    """
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    bpmn_diagram = BpmnDiagram()

    processes = root.findall(BpmnXmlElement.PROCESS.value)
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

        for xml_child in process_xml:
            element = None
            if xml_child.tag == BpmnXmlElement.START_EVENT.value:
                element = StartEvent(xml_child)
            if xml_child.tag == BpmnXmlElement.END_EVENT.value:
                element = EndEvent(xml_child)
            if xml_child.tag == BpmnXmlElement.PARALLEL_GATEWAY.value:
                element = ParallelGateway(xml_child)
            if xml_child.tag == BpmnXmlElement.EVENT_BASED_GATEWAY.value:
                element = EventBasedGateway(xml_child)
            if xml_child.tag == BpmnXmlElement.INTERMEDIATE_CATCH_EVENT.value:
                element = IntermediateEvent(xml_child)
            if xml_child.tag == BpmnXmlElement.TASK.value:
                element = Task(xml_child, xml_child.attrib.get('startQuantity'))
            append = False
            if element is not None:
                for lane in process.lanes:
                    for e_id in lane.elements_ids:
                        if e_id == element.element_id and append is False:
                            lane_index = process.lanes.index(lane)
                            process_index = bpmn_diagram.processes.index(process)
                            lane.append_element(element)
                            append = True

                if append is False:
                    process.append_element(element)

            if xml_child.tag == BpmnXmlElement.SEQUENCE_FLOW.value:
                source_ref = xml_child.attrib.get('sourceRef')
                target_ref = xml_child.attrib.get('targetRef')
                source_found = False
                target_found = False
                source = None
                target = None
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

                flow = SequenceFlow(xml_child, source, target, 0)
                process.append_element(flow)

    collaboration = root.find(BpmnXmlElement.COLLABORATION.value)
    for xml_child in collaboration:
        if xml_child.tag == BpmnXmlElement.MESSAGE_FLOW.value:
            source_ref = xml_child.attrib.get('sourceRef')
            target_ref = xml_child.attrib.get('targetRef')
            target_found = False
            source_found = False
            target = None
            source = None
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

            message_flow = MessageFlow(xml_child, source, target)
            bpmn_diagram.append_element(message_flow)

        if xml_child.tag == BpmnXmlElement.PARTICIPANT.value:
            for process in bpmn_diagram.processes:
                if process.process_id == xml_child.attrib.get('processRef'):
                    process.name = get_name(xml_child)

    print(bpmn_diagram)

    return bpmn_diagram


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
    parse_bpmn_file('pizza-collaboration.bpmn')
    # Convertir en réseau de Petri
# petri_net = bpmn_to_petri(bpmn_diagram)
# Créer un graphique du réseau de Petri
# petri_net_to_graph(petri_net, 'petri_net.png')

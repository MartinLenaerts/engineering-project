from classes.BPMN.bpmn_element import BPMNElement
from constant.bpmn_xml_elements import BpmnXmlElement


class FlowObject(BPMNElement):
    def __init__(self, xml_element):
        super().__init__(xml_element)

        self.incoming_elements = []
        self.outgoing_elements = []
        self.incoming_ids = []
        self.outgoing_ids = []

        for xml_child in xml_element:
            if xml_child.tag == BpmnXmlElement.OUTGOING.value:
                self.incoming_ids.append(xml_child.text)

            if xml_child.tag == BpmnXmlElement.INCOMING.value:
                self.outgoing_ids.append(xml_child.text)

    def append_incoming_element(self, element):
        self.incoming_elements.append(element)

    def append_outgoing_element(self, element):
        self.outgoing_elements.append(element)

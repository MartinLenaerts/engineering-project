from classes.BPMN.flow.flow_object import FlowObject


class SubProcess(FlowObject):
    def __init__(self, xml_element):
        super().__init__(xml_element)
        self.elements = []

    def append_element(self, element):
        self.elements.append(element)

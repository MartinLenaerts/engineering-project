from classes.BPMN.bpmn_element import BPMNElement


class Lane(BPMNElement):
    def __init__(self, xml_element, elements_ids):
        super().__init__(xml_element)
        self.elements_ids = elements_ids
        self.elements = []

    def append_element(self, element):
        self.elements.append(element)

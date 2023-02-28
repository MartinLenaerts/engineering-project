from classes.BPMN.bpmn_element import BPMNElement


class FlowObject(BPMNElement):
    def __init__(self, xml_element):
        super().__init__(xml_element)

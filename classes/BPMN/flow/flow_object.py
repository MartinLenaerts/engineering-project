from classes.BPMN.bpmn_element import BPMNElement


class FlowObject(BPMNElement):
    def __init__(self, element_id, name):
        super().__init__(element_id)
        self.name = name

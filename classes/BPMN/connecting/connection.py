from classes.BPMN.bpmn_element import BPMNElement


class Connection(BPMNElement):
    def __init__(self, name, source, target, element_id):
        super().__init__(element_id)
        self.name = name
        self.source = source
        self.target = target

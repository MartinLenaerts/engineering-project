from classes.BPMN.bpmn_element import BPMNElement


class Connection(BPMNElement):
    def __init__(self, xml_element, source, target):
        super().__init__(xml_element)
        self.source = source
        self.target = target

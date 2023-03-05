from classes.BPMN.bpmn_element import BPMNElement


class Connection(BPMNElement):
    def __init__(self, xml_element, source, target):
        super().__init__(xml_element)
        self.source = source
        self.target = target

        target.append_incoming_element(self)
        source.append_outgoing_element(self)

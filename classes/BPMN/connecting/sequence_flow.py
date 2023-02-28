from classes.BPMN.connecting.connection_flow import Connection


class SequenceFlow(Connection):
    def __init__(self, xml_element, source, target, quantity):
        super().__init__(xml_element, source, target)
        self.quantity = quantity

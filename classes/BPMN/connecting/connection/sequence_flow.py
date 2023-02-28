from classes.BPMN.connecting.connection import Connection


class SequenceFlow(Connection):
    def __init__(self, name, source, target, quantity, element_id):
        super().__init__(name, source, target, element_id)
        self.quantity = quantity

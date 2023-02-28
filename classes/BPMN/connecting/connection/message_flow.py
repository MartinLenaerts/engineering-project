from classes.BPMN.connecting.connection import Connection


class MessageFlow(Connection):
    def __init__(self, name, source, target, element_id):
        super().__init__(name, source, target, element_id)

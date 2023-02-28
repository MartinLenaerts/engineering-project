from classes.BPMN.connecting.connection_flow import Connection


class MessageFlow(Connection):
    def __init__(self, xml_element, source, target):
        super().__init__(xml_element, source, target)

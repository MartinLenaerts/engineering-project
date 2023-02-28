from classes.BPMN.connecting.connection_flow import Connection


class Association(Connection):
    def __init__(self, xml_element, source, target):
        super().__init__(xml_element, source, target)

from classes.BPMN.flow.flow_object import FlowObject


class Gateway(FlowObject):
    def __init__(self, xml_element, gateway_type):
        super().__init__(xml_element)
        self.type = gateway_type

from classes.BPMN.flow.flow_object import FlowObject


class Gateway(FlowObject):
    def __init__(self, element_id, name, gateway_type):
        super().__init__(element_id, name)
        self.type = gateway_type

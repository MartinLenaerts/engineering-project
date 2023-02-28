from classes.BPMN.flow.flow_object import FlowObject


class Event(FlowObject):
    def __init__(self, element_id, name, event_type):
        super().__init__(element_id, name)
        self.event_type = event_type

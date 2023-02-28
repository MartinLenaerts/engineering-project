from classes.BPMN.flow.flow_object import FlowObject


class Event(FlowObject):
    def __init__(self, xml_element, event_type):
        super().__init__(xml_element)
        self.event_type = event_type

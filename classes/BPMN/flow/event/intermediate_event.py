from classes.BPMN.flow.event.event import Event
from constant.event_type import EventType


class IntermediateEvent(Event):
    def __init__(self, xml_element):
        super().__init__(xml_element, EventType.INTERMEDIATE)
        self.incoming_id = []
        self.incoming_element = []
        self.outgoing_id = []
        self.outgoing_element = []

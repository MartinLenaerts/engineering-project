from classes.BPMN.flow.event.event import Event
from constant.event_type import EventType


class EndEvent(Event):
    def __init__(self, xml_element):
        super().__init__(xml_element, EventType.END)

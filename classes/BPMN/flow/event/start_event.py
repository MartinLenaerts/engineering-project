from classes.BPMN.flow.event.event import Event


class StartEvent(Event):
    def __init__(self, element_id, name, event_type):
        super().__init__(element_id, name, event_type)
from classes.BPMN.flow.flow_object import FlowObject


class Activity(FlowObject):
    def __init__(self, element_id, name, activity_type, start_quantity):
        super().__init__(element_id, name)
        self.activity_type = activity_type
        self.start_quantity = start_quantity

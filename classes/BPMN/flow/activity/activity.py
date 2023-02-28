from classes.BPMN.flow.flow_object import FlowObject


class Activity(FlowObject):
    def __init__(self, xml_element, activity_type, start_quantity):
        super().__init__(xml_element)
        self.activity_type = activity_type
        self.start_quantity = start_quantity

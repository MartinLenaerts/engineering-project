from classes.BPMN.flow.activity.activity import Activity


class Task(Activity):

    def __init__(self, element_id, name, activity_type, start_quantity):
        super().__init__(element_id, name, activity_type, start_quantity)
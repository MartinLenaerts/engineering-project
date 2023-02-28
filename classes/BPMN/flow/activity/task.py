from classes.BPMN.flow.activity.activity import Activity
from constant.activity_type import ActivityType


class Task(Activity):

    def __init__(self, xml_element, start_quantity):
        super().__init__(xml_element, ActivityType.TASK, start_quantity)

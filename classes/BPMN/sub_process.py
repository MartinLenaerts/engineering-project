from utils.functions import get_id, get_name


class Process:

    def __init__(self, xml_element):
        self.name = get_name(xml_element)
        self.process_id = get_id(xml_element)
        self.lanes = []
        self.elements = []

    def append_lane(self, lane):
        self.lanes.append(lane)

    def append_element(self, element):
        self.elements.append(element)

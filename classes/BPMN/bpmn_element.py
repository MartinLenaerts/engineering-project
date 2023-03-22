from utils.xml_functions import get_id, get_name


class BPMNElement:
    def __init__(self, xml_element):
        self.element_id = get_id(xml_element)
        self.name = get_name(xml_element)

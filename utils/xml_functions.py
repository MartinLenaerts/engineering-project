

def get_name(xml_element):
    return xml_element.attrib.get('name')


def get_id(xml_element):
    return xml_element.attrib.get('id')
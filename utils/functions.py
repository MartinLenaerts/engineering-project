import os


def get_name(xml_element):
    return xml_element.attrib.get('name')


def get_id(xml_element):
    return xml_element.attrib.get('id')


def get_files_from_dir(dir_path):
    res = []
    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isfile(path):
            file_name, file_extension = os.path.splitext(path)
            if file_extension == ".bpmn_diagrams":
                res.append(path)
        elif os.path.isdir(path):
            res = res + get_files_from_dir(path)

    return res

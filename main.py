import os

from utils.bpmn_functions import parse_bpmn_file
from utils.functions import get_files_from_dir
from utils.translation_functions import bpmn_to_petri

if __name__ == '__main__':
    dir_path = 'docs/bpmn'

    print(get_files_from_dir(dir_path))
    for path in get_files_from_dir(dir_path):
        file_name, file_extension = os.path.splitext(path)

        bpmn_diagram = parse_bpmn_file(path)
        print(bpmn_diagram)
        bpmn_to_petri(bpmn_diagram, file_name.replace('/bpmn', '/petri'))

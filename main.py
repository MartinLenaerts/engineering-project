import getopt
import logging
import os
import sys

from utils.bpmn_functions import parse_bpmn_file
from utils.env import load_and_check_env
from utils.utils_functions import get_files_from_dir
from utils.petri_functions import petri_net_to_graph
from utils.translation_functions import bpmn_to_petri

logs_file, petri_output_dir = load_and_check_env()

logging.basicConfig(filename=logs_file, level=logging.INFO)


def get_args(argv):
    opts, args = getopt.getopt(argv, "hf:", ["filename="])
    filename = None
    for opt, arg in opts:
        if opt == '-h':
            logging.info('main.py -f <bpmn_diagrams file name>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
    logging.info('Arguments ==>  {}'.format(filename))

    return filename


if __name__ == '__main__':
    logging.info("\r\n\r\n################## New Execution ##################")
    dir_path = 'resources/bpmn_diagrams'

    filename_arg = get_args(sys.argv[1:])
    print(get_files_from_dir(dir_path))
    for path in get_files_from_dir(dir_path):
        file_name, file_extension = os.path.splitext(path)
        filename_without_ext, _ = os.path.splitext(os.path.basename(file_name))
        print(filename_without_ext, filename_arg)
        if filename_arg is None or filename_without_ext == filename_arg:
            logging.info("\r\n !!!!!! file : {} !!!!!! ".format(path))

            bpmn_diagram = parse_bpmn_file(path)

            logging.info("{} file parsed".format(filename_without_ext))
            petri_net = bpmn_to_petri(bpmn_diagram)

            logging.info("{} petri net generated".format(filename_without_ext))

            img_path = "{}.png".format(file_name.replace(dir_path, petri_output_dir))
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            petri_net_to_graph(petri_net, img_path)

            logging.info("{} petri net save in png ({})".format(filename_without_ext, img_path))

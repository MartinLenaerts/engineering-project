import getopt
import logging
import os
import sys

from utils.bpmn_functions import parse_bpmn_file
from utils.functions import get_files_from_dir
from utils.petri_functions import petri_net_to_graph
from utils.translation_functions import bpmn_to_petri

logging.basicConfig(filename="cache/logs/main.log", level=logging.INFO)


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
    for path in get_files_from_dir(dir_path):
        file_name, file_extension = os.path.splitext(path)
        filename_without_ext, _ = os.path.splitext(os.path.basename(file_name))

        if filename_arg is None or filename_without_ext == filename_arg:
            logging.info("\r\n !!!!!! file : {} !!!!!! ".format(path))

            bpmn_diagram = parse_bpmn_file(path)

            logging.info("{} file parsed".format(filename_without_ext))
            petri_net = bpmn_to_petri(bpmn_diagram)

            logging.info("{} petri_output net generated".format(filename_without_ext))

            img_path = "{}.png".format(file_name.replace(dir_path, 'cache/petri_output'))
            petri_net_to_graph(petri_net, img_path)

            logging.info("{} petri_output net save in png ({})".format(filename_without_ext, img_path))

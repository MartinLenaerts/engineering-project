import getopt
import logging
import os
import sys
import traceback

from utils.bpmn_functions import parse_bpmn_file
from utils.env import load_and_check_env
from utils.utils_functions import get_files_from_dir
from utils.petri_functions import petri_net_to_img, petri_net_to_text
from utils.translation_functions import bpmn_to_petri

logs_file, petri_output_dir = load_and_check_env()

logging.basicConfig(filename=logs_file, level=logging.INFO)


def get_args(argv):
    opts, args = getopt.getopt(argv, "hf:o:", ["filename=", "output="])
    filename = None
    output = "png"
    for opt, arg in opts:
        if opt == '-h':
            logging.info('main.py -f <bpmn_diagrams file name> -o <output type (png or txt)')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-o", "--output"):
            output = arg
    logging.info('Arguments ==>  filename: {}, output: {}'.format(filename, output))

    return filename, output


if __name__ == '__main__':
    logging.info("\r\n\r\n################## New Execution ##################")
    dir_path = 'resources/bpmn_diagrams'

    filename_arg, output_arg = get_args(sys.argv[1:])
    for path in get_files_from_dir(dir_path):
        file_name, file_extension = os.path.splitext(path)
        filename_without_ext, _ = os.path.splitext(os.path.basename(file_name))
        if filename_arg is None or filename_without_ext == filename_arg:
            try:
                logging.info("\r\n !!!!!! file : {} !!!!!! ".format(path))

                bpmn_diagram = parse_bpmn_file(path)

                logging.info("{} file parsed".format(filename_without_ext))
                petri_net = bpmn_to_petri(bpmn_diagram)

                logging.info("{} petri net generated".format(filename_without_ext))

                if output_arg == "txt":
                    img_path = "{}.txt".format(file_name.replace(dir_path, petri_output_dir))
                    os.makedirs(os.path.dirname(img_path), exist_ok=True)
                    petri_net_to_text(petri_net, img_path)
                else:
                    img_path = "{}.png".format(file_name.replace(dir_path, petri_output_dir))
                    os.makedirs(os.path.dirname(img_path), exist_ok=True)
                    petri_net_to_img(petri_net, img_path)

                logging.info("✅ {} petri net save in png ({}) ✅".format(filename_without_ext, img_path))
            except Exception as e:
                logging.error("‼️ Error in {} file, Message : '{}' ‼️".format(filename_without_ext, e))
                logging.error(traceback.format_exc())


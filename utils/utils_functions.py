import getopt
import logging
import os
import sys
import traceback

from utils.bpmn_functions import parse_bpmn_file
from utils.petri_functions import petri_net_to_text, petri_net_to_img
from utils.translation_functions import bpmn_to_petri


def get_files_from_dir(dir_path):
    res = []
    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isfile(path):
            file_name, file_extension = os.path.splitext(path)
            if file_extension == ".bpmn":
                res.append(path)
        elif os.path.isdir(path):
            res = res + get_files_from_dir(path)

    return res


def parse_and_translate_from_file(filename_arg, output_type, output_dir):
    dir_path = 'resources/bpmn_diagrams'

    for path in get_files_from_dir(dir_path):
        file_name, file_extension = os.path.splitext(path)
        filename_without_ext, _ = os.path.splitext(os.path.basename(file_name))
        if filename_arg is None or filename_without_ext == filename_arg:
            try:
                logging.debug("\r\n !!!!!! file : {} !!!!!! ".format(path))

                bpmn_diagram = parse_bpmn_file(path)

                logging.debug("{} file parsed".format(filename_without_ext))
                petri_net = bpmn_to_petri(bpmn_diagram)

                logging.debug("{} petri net generated".format(filename_without_ext))

                if output_type == "txt":
                    img_path = "{}.txt".format(file_name.replace(dir_path, output_dir))
                    os.makedirs(os.path.dirname(img_path), exist_ok=True)
                    petri_net_to_text(petri_net, img_path)
                else:
                    img_path = "{}.png".format(file_name.replace(dir_path, output_dir))
                    os.makedirs(os.path.dirname(img_path), exist_ok=True)
                    petri_net_to_img(petri_net, img_path)

                logging.info("✅ {} petri net save in png ({}) ✅".format(filename_without_ext, img_path))
            except Exception as e:
                logging.critical("‼️ Error in {} file, Message : '{}' ‼️".format(filename_without_ext, e))
                logging.error(traceback.format_exc())


def get_args(argv):
    opts, args = getopt.getopt(argv, "hf:o:", ["filename=", "output="])
    filename = None
    output = "png"
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -f <bpmn_diagrams file name> -o <output type (png or txt)')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-o", "--output"):
            output = arg
    logging.debug('Arguments ==>  filename: {}, output: {}'.format(filename, output))

    return filename, output

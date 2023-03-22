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


def parse_and_translate_from_file(filename, output_type, output_dir):
    file_name, _ = os.path.splitext(filename)
    filename_without_ext, a = os.path.splitext(os.path.basename(file_name))

    try:
        logging.debug("\r\n !!!!!! file : {} !!!!!! ".format(filename))

        bpmn_diagram = parse_bpmn_file(filename)

        logging.debug("{} file parsed".format(filename_without_ext))
        petri_net = bpmn_to_petri(bpmn_diagram)

        logging.debug("{} petri net generated".format(filename_without_ext))

        files_created = []
        if output_dir is not None:
            filepath = file_name.replace(os.path.dirname(filename), output_dir)
        else:
            filepath = file_name
        if output_type is None or (output_type == "txt"):
            txt_path = "{}.txt".format(filepath)
            os.makedirs(os.path.dirname(txt_path), exist_ok=True)
            petri_net_to_text(petri_net, txt_path)
            files_created.append(txt_path)

        if output_type is None or (output_type == "png"):
            img_path = "{}.png".format(filepath)
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            petri_net_to_img(petri_net, img_path)
            files_created.append(img_path)

        logging.info("✅ {} petri net save in png ({}) ✅".format(filename_without_ext, ', '.join(files_created)))
    except Exception as e:
        logging.critical("‼️ Error in {} file, Message : '{}' ‼️".format(filename_without_ext, e))
        logging.error(traceback.format_exc())


def parse_and_translate(filename_arg, output_type, output_dir):
    default_dir_path = 'resources/bpmn_diagrams'

    if filename_arg is None:
        filename_arg = default_dir_path

    if not os.path.exists(filename_arg) and os.path.exists("{}/{}.bpmn".format(default_dir_path, filename_arg)):
        filename_arg = "{}/{}.bpmn".format(default_dir_path, filename_arg)

    if os.path.isdir(filename_arg):
        for path in get_files_from_dir(filename_arg):
            parse_and_translate_from_file(path, output_type, output_dir)
    else:
        parse_and_translate_from_file(filename_arg, output_type, output_dir)


def get_args(argv):
    opts, args = getopt.getopt(argv, "hf:o:k", ["filename=", "output="])
    filename = None
    output = None
    keep = False
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -f <bpmn_diagrams file name> -o <output type (png or txt)>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-k", "--keep"):
            keep = True
    logging.debug('Arguments ==>  filename: {}, output: {}, keep: {}'.format(filename, output, keep))

    return filename, output, keep

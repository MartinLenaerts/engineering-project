import logging
import os
import traceback
import argparse

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


def get_args(petri_output_dir):
    parser = argparse.ArgumentParser(description="Script to translate bpmn diagram to petri net")

    parser.add_argument('-f', '--filename', action='store', dest='filename', default=None, type=str,
                        help='BPMN file to translate (.bpmn file), if this argument is not given, all the files in the '
                             'folder "resources/bpmn_diagrams" will be translated')
    parser.add_argument('-o', '--output', action='store', dest='output', default=None, type=str, choices=['png', 'txt'],
                        help='output type (png or txt)')
    parser.add_argument('--keep', action='store_true', dest='keep',
                        help='Save the output file(s) in the same location as the .bpmn file. if this argument is not '
                             'given, the file(s) will be saved here: "{}"'.format(petri_output_dir))

    args = parser.parse_args()
    logging.debug('Arguments ==>  filename: {}, output: {}, keep: {}'.format(args.filename, args.output, args.keep))

    return args

import logging
import sys
from utils.env import load_and_check_env
from utils.utils_functions import get_args, parse_and_translate_from_file

if __name__ == '__main__':
    logs_file, petri_output_dir = load_and_check_env()

    logging.basicConfig(filename=logs_file, level=logging.DEBUG)

    logging.debug("\r\n\r\n################## New Execution ##################")
    filename_arg, output_arg = get_args(sys.argv[1:])

    parse_and_translate_from_file(filename_arg, output_arg, petri_output_dir)

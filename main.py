import logging
from utils.env import load_and_check_env
from utils.utils_functions import get_args, parse_and_translate

if __name__ == '__main__':
    logs_file, petri_output_dir = load_and_check_env()

    logging.basicConfig(filename=logs_file, level=logging.DEBUG)

    logging.debug("\r\n\r\n################## New Execution ##################")
    args = get_args(petri_output_dir)

    if args.keep:
        petri_output_dir = None

    parse_and_translate(args.filename, args.output, petri_output_dir)

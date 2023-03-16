import os
from dotenv import load_dotenv


def load_and_check_env():
    load_dotenv()

    logs_file = os.getenv('LOGS_FILE')
    petri_output_dir = os.getenv('PETRI_OUTPUT_DIR')
    try:
        os.makedirs(os.path.dirname(logs_file), exist_ok=True)
        open(logs_file, "x")
    except (Exception,):
        pass
    if os.path.exists(petri_output_dir) is False:
        os.makedirs(petri_output_dir, exist_ok=True)

    return logs_file, petri_output_dir

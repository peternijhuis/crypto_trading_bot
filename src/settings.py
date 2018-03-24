import os

# data folder by scenario dependent, not synced with git
DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# data pipeline
INPUT_DATA = os.path.join(DATA_FOLDER, '0_input')
RAW_DATA = os.path.join(DATA_FOLDER, '1_raw')
PREPROCESSED_DATA = os.path.join(DATA_FOLDER, '2_preprocessed')
OUTPUT_DATA = os.path.join(DATA_FOLDER, '3_output')

# additional folders
# TMP_DATA = os.path.join(DATA_FOLDER, 'tmp_data')
# LOG_DATA_FOLDER = os.path.join(DATA_FOLDER, 'log_data')
# print(DATA_FOLDER)

# create if needed
def _create_if_needed(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

_create_if_needed(INPUT_DATA)
_create_if_needed(RAW_DATA)
_create_if_needed(PREPROCESSED_DATA)
_create_if_needed(OUTPUT_DATA)
# _create_if_needed(TMP_DATA)
# _create_if_needed(LOG_DATA_FOLDER)
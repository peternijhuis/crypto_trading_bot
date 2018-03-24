"""
    General utilities used throughout codes
"""
import json
import os
import logging
# from src.settings import *
import sys
import math

logger = logging.getLogger(__name__)


def print_json(data):
    # pretty prints trips
    print(json.dumps(data, sort_keys=True, indent=4))

def write_file(data, file, folder):
    if not os.path.exists(folder):
                os.makedirs(folder)
    with open('{}/{}'.format(folder, file), 'w') as save_result:
                save_result.write('{}'.format(data))


def load_json(file, input_folder, print_result=False, refactor_keys=False):
    # refactor keys: to put keys from strings to ints, common for units.json
    # with open('%s/%s.json' % (input_folder, file), 'r') as data_file:
    if not file.endswith('.json'):
        file += '.json'
    with open(os.path.join(input_folder, file), 'r') as data_file:
        json_data = json.load(data_file)
    if print_result:
        print('\n\n----> File %s is printed:' % file)
        print_json(json_data)

    if refactor_keys:
        return {int(id): data for id, data in json_data.items()}
    else:
        return json_data


def save_json(data, file, folder):
    if not os.path.exists(folder):
        os.makedirs(folder, True)
    if not file.endswith('.json'):
        file += '.json'
    with open(os.path.join(folder, file), 'w') as fp:
        # json.dump(data, fp, indent=4, encoding='utf-8')
        # utf-8 does not work with parse_gebieden @peter
        json.dump(data, fp, indent=4, encoding='iso-8859-1')

def save_json_less_overhead(data, file, folder):
    with open(os.path.join(folder, file), 'w') as fp:
        json.dump(data, fp, indent=4, encoding='utf-8')
        # utf-8 does not work with parse_gebieden @peter
        # json.dump(data, fp, indent=4, encoding='iso-8859-1')

def save_non_python_object_to_json(data, file, folder):
    # more info: https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/
    def jdefault(o):
        return o.__dict__
    json.dump(data, os.path.join(folder, file), indent=4, encoding='utf-8', default=jdefault)


def progress_bar(progress):
    """
    Input your progress like 0.03 and this function converts it to a progress bar output
    """
    sys.stdout.write("\r[%-20s] %d%%" % ('='*int(math.floor(20 * progress)), 100*progress))
    sys.stdout.flush()

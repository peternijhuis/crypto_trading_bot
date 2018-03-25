#! /usr/bin/env python
# Import packages
import sys
import os
import json
import glob

from src.settings import RAW_DATA
from src.settings import PREPROCESSED_DATA

# locate the root folder
root_folder_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# add the root folder to sys path, this way the different modules can be imported by UNIX!
sys.path.insert(1, root_folder_project)


"""
Combine multiple files together to create one file. The OHLCV minute data has overlap. Only register one entry and
remove all duplicates.

Combined file resides in pre-processed folder

Bulk and / or incremental?

"""

# Specify the path
path = os.path.join(RAW_DATA,'ADA')

# Returns the filenames including the paths to the regex string in the specified folder
paths = glob.glob("{}/*.json".format(path))

# Glob returns the path with regex, os.path.basename strips the path thus only keeping the file name
names = [os.path.basename(x) for x in glob.glob("{}/*.json".format(path))]

ADA = {}

for pathnames in paths:
    with open(pathnames, 'r') as data_file:
        json_data = json.load(data_file)
        ADA.update(json_data)

# update does not work for now..



# with open(os.path.join(RAW_DATA, file), 'r') as data_file:
#     json_data = json.load(data_file)
#
#
#
# filename = '{}_to_{}_{}_OHLCV.json'.format(start, end, ticker)
# path = os.path.join(folder, filename)
# if not os.path.exists(folder):
#     os.makedirs(folder)
# with open(path, 'w') as fp:
#     json.dump(ticker_data_json, fp, sort_keys=True, indent=4)
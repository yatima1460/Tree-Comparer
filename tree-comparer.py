#!/usr/bin/python3

import sys
import getopt
from os import listdir
from os.path import isfile, join
import os.path
import logging
from pathlib import Path

print()

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def get_parent(path: str) -> str:
    path = Path(path)
    return str(path.parent.absolute())


def compare(reference_directory, test_directory):

    logging.debug(f'Compare {reference_directory} => {test_directory}')

    reference_directory_parent = get_parent(reference_directory)
    test_directory_parent = get_parent(test_directory)
    
    listed_dir = None
    
    try:
        listed_dir = listdir(reference_directory)
    except PermissionError as e:
        logging.error(f'Can\'t read directory {e}')
        return

    for relative_file_path in listed_dir:



        file_reference_directory = join(
            reference_directory, relative_file_path)
        file_test_directory = join(test_directory, relative_file_path)

        if os.path.isdir(file_reference_directory):
            logging.debug(f'CheckDir {file_reference_directory} => {file_test_directory}')
            if os.path.isdir(file_test_directory):
                logging.debug(f'Directory {file_reference_directory} => {file_test_directory} exists')
                compare(file_reference_directory, file_test_directory)
            else:
                logging.error(f'Directory "{file_reference_directory}" => does not exist in "{test_directory}"')
        if os.path.isfile(file_reference_directory):
            if os.path.isfile(file_test_directory):
                logging.debug(f'File {file_reference_directory} => {file_test_directory} exists')
                reference_size = os.path.getsize(file_reference_directory)
                test_size = os.path.getsize(file_test_directory)
                if test_size != reference_size:
                    logging.warn(f'File size mismatch {file_reference_directory} ({reference_size} bytes) and {file_test_directory} ({test_size} bytes)')
            else:
                logging.error(f'File      "{file_reference_directory}" => does not exist in "{test_directory}"')


def main(argv):
    inputfile = argv[1]
    outputfile = argv[2]
    logging.debug(f'Input dir is "{inputfile}" ')
    logging.debug(f'Output dir is "{outputfile}" ')
    compare(inputfile, outputfile)
    compare(outputfile, inputfile)


if __name__ == "__main__":
   main(sys.argv)

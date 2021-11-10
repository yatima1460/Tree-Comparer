#!/usr/bin/python3

import hashlib
import logging
import os
import sys

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
BUF_SIZE = 65536  # 64kb chunks

def hash(file: str) -> str:

    sha1 = hashlib.sha1()

    try:
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return format(sha1.hexdigest())
    except Exception as e:
        logging.critical(e)
        return "<invalid-hash>"


def compare(reference_directory: str, test_directory: str):
    
    if not isinstance(reference_directory, str):
        logging.critical("Invalid reference directory")
        return
    if not isinstance(test_directory, str):
        logging.critical("Invalid test directory")
        return
    if reference_directory == test_directory:
        return

    listed_dir = None
    try:
        listed_dir = os.listdir(reference_directory)
    except Exception as e:
        logging.critical(e)
        return

    for relative_file_path in listed_dir:

        relative_reference_file = os.path.join(reference_directory, relative_file_path)
        file_test_directory = os.path.join(test_directory, relative_file_path)

        # If the reference file is a regular file
        if os.path.isfile(relative_reference_file):

            # Check if a regular file exists on other side as well
            if not os.path.isfile(file_test_directory):
                logging.error(f'File      "{relative_reference_file}" => does not exist in "{test_directory}"')
                continue
            
            # Check if the sizes match
            reference_size = os.path.getsize(relative_reference_file)
            test_size = os.path.getsize(file_test_directory)
            if test_size != reference_size:
                logging.warning(f'File size mismatch {relative_reference_file} ({reference_size} bytes) and {file_test_directory} ({test_size} bytes)')
                continue
            
            # Check if the hashes match
            reference_hash = hash(relative_reference_file)
            test_hash = hash(file_test_directory)
            if reference_hash != test_hash:
                logging.warn(f'File hash mismatch "{relative_reference_file}" ({reference_hash}) and "{file_test_directory}" ({test_hash})')
                continue

        # If the reference file is a directory
        if os.path.isdir(relative_reference_file):

            # Check if a directory exists on other side as well
            if not os.path.isdir(file_test_directory):
                logging.error(f'Directory "{relative_reference_file}" => does not exist in "{test_directory}"')
                continue
 
            compare(relative_reference_file, file_test_directory)
            
        # If the reference file is a link file
        if os.path.islink(relative_reference_file):
    
            # Check if a link file exists on other side as well
            if not os.path.islink(file_test_directory):
                logging.error(f'Link      "{relative_reference_file}" => does not exist in "{test_directory}"')
                continue

def main(argv):
    inputfile = argv[1]
    outputfile = argv[2]

    compare(inputfile, outputfile)
    compare(outputfile, inputfile)


if __name__ == "__main__":
    main(sys.argv)

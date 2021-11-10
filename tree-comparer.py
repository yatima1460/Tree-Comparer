#!/usr/bin/python3

import hashlib
import logging
import os
import sys

# Buffer size used when calculating the hash
BUF_SIZE = 65536  # 64kb chunks

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

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


def compare(reference: str, test: str, check_size = True, check_hash = True):
    
    if not isinstance(reference, str):
        logging.critical("Invalid reference directory")
        return
    if not isinstance(test, str):
        logging.critical("Invalid test directory")
        return
    if reference == test:
        return

    listed_reference = None
    try:
        listed_reference = os.listdir(reference)
    except Exception as e:
        logging.critical(e)
        return

    # Compare first relative to test
    for relative_reference_file in listed_reference:

        absolute_reference_file = os.path.join(reference, relative_reference_file)
        absolute_test_file = os.path.join(test, relative_reference_file)

        # If the reference file is a regular file
        if os.path.isfile(absolute_reference_file):

            # Check if a regular file exists on other side as well
            if not os.path.isfile(absolute_test_file):
                logging.error(f'File      "{absolute_reference_file}" => does not exist in "{test}"')
                continue
            
            # Check if the sizes match
            if check_size:
                reference_size = os.path.getsize(absolute_reference_file)
                test_size = os.path.getsize(absolute_test_file)
                if test_size != reference_size:
                    logging.warning(f'File size mismatch {absolute_reference_file} ({reference_size} bytes) and {absolute_test_file} ({test_size} bytes)')
                    continue
            
            # Check if the hashes match
            if check_hash:
                reference_hash = hash(absolute_reference_file)
                test_hash = hash(absolute_test_file)
                if reference_hash != test_hash:
                    logging.warn(f'File hash mismatch "{absolute_reference_file}" ({reference_hash}) and "{absolute_test_file}" ({test_hash})')
                    continue

        # If the reference file is a directory
        if os.path.isdir(absolute_reference_file):

            # Check if a directory exists on other side as well
            if not os.path.isdir(absolute_test_file):
                logging.error(f'Directory "{absolute_reference_file}" => does not exist in "{test}"')
                continue
 
            compare(absolute_reference_file, absolute_test_file, check_size, check_hash)
            
        # If the reference file is a link file
        if os.path.islink(absolute_reference_file):
    
            # Check if a link file exists on other side as well
            if not os.path.islink(absolute_test_file):
                logging.error(f'Link      "{absolute_reference_file}" => does not exist in "{test}"')
                continue


def main(argv):
    if len(argv) != 2:
        logging.critical("Wrong input arguments count")
        return
    reference = argv[0]
    test = argv[1]

    # Normal reference to test comparison
    compare(reference, test)
    
    # Useful to check if some files that exist in test shouldn't actually exist
    compare(test, reference, check_size = False, check_hash = False)


if __name__ == "__main__":
    main(sys.argv[1:])

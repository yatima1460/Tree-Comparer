#!/usr/bin/python3

import hashlib
import logging
import os
import sys

# Buffer size used when calculating the hash
BUF_SIZE = 65536  # 64kb chunks

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def hash(FILE: str) -> str:
    sha1 = hashlib.sha1()
    try:
        with open(FILE, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return format(sha1.hexdigest())
    except Exception as e:
        logging.critical(e)
        return "<invalid-hash>"


def compare(REFERENCE : str, TEST: str, CHECK_SIZE = True, CHECK_HASH = True):

    if not isinstance(REFERENCE, str):
        logging.critical("Invalid reference directory")
        return
    if not isinstance(TEST, str):
        logging.critical("Invalid test directory")
        return
    if REFERENCE == TEST:
        return

    listed_reference = None
    try:
        listed_reference = os.listdir(REFERENCE)
    except Exception as e:
        logging.critical(e)
        return

    # Compare first relative to test
    for RELATIVE_REFERENCE_FILE in listed_reference:

        ABSOLUTE_REFERENCE_FILE = os.path.join(REFERENCE, RELATIVE_REFERENCE_FILE)
        ABSOLUTE_TEST_FILE = os.path.join(TEST, RELATIVE_REFERENCE_FILE)

        # If the reference file is a regular file
        if os.path.isfile(ABSOLUTE_REFERENCE_FILE):

            # Check if a regular file exists on other side as well
            if not os.path.isfile(ABSOLUTE_TEST_FILE):
                logging.error(f'File      "{ABSOLUTE_REFERENCE_FILE}" => does not exist in "{TEST}"')
                continue
            
            # Check if the sizes match
            if CHECK_SIZE:
                REFERENCE_SIZE = os.path.getsize(ABSOLUTE_REFERENCE_FILE)
                TEST_SIZE = os.path.getsize(ABSOLUTE_TEST_FILE)
                if TEST_SIZE != REFERENCE_SIZE:
                    logging.warning(f'File size mismatch {ABSOLUTE_REFERENCE_FILE} ({REFERENCE_SIZE} bytes) and {ABSOLUTE_TEST_FILE} ({TEST_SIZE} bytes)')
                    continue
            
            # Check if the hashes match
            if CHECK_HASH:
                REFERENCE_HASH = hash(ABSOLUTE_REFERENCE_FILE)
                TEST_HASH = hash(ABSOLUTE_TEST_FILE)
                if REFERENCE_HASH != TEST_HASH:
                    logging.warn(f'File hash mismatch "{ABSOLUTE_REFERENCE_FILE}" ({REFERENCE_HASH}) and "{ABSOLUTE_TEST_FILE}" ({TEST_HASH})')
                    continue

        # If the reference file is a directory
        if os.path.isdir(ABSOLUTE_REFERENCE_FILE):

            # Check if a directory exists on other side as well
            if not os.path.isdir(ABSOLUTE_TEST_FILE):
                logging.error(f'Directory "{ABSOLUTE_REFERENCE_FILE}" => does not exist in "{TEST}"')
                continue
 
            compare(ABSOLUTE_REFERENCE_FILE, ABSOLUTE_TEST_FILE, CHECK_SIZE, CHECK_HASH)
            
        # If the reference file is a link file
        if os.path.islink(ABSOLUTE_REFERENCE_FILE):
    
            # Check if a link file exists on other side as well
            if not os.path.islink(ABSOLUTE_TEST_FILE):
                logging.error(f'Link      "{ABSOLUTE_REFERENCE_FILE}" => does not exist in "{TEST}"')
                continue


def main(argv):
    if len(argv) != 2:
        logging.critical("Wrong input arguments count")
        return
    REFERENCE = argv[0]
    TEST = argv[1]

    # Normal reference to test comparison
    compare(REFERENCE, TEST)
    
    # Useful to check if some files that exist in test shouldn't actually exist
    compare(TEST, REFERENCE, CHECK_SIZE = False, CHECK_HASH = False)


if __name__ == "__main__":
    main(sys.argv[1:])

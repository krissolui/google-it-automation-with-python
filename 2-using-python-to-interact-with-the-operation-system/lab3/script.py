#!/usr/bin/env python3

import sys
import os
import re

# Month Day hour:minute:second mycomputername "process_name"["ra$


def get_error_type():
    while True:
        error = input("What is the error? ")
        if len(error) > 0:
            break

    return error


def error_search(log_file):
    error = get_error_type()
    error_patterns = ["error"]
    error_list = error.split(" ")
    for error_item in error_list:
        error_patterns.append(r"" + error_item.lower())
    returned_errors = []

    with open(log_file, encoding="UTF-8") as file:
        for line in file.readlines():
            if all(
                re.search(error_pattern, line.lower())
                for error_pattern in error_patterns
            ):
                returned_errors.append(line)

    return returned_errors


def file_output(returned_errors):
    with open(os.path.expanduser("~") + "/data/errors_found.log", "w") as file:
        for error in returned_errors:
            file.write(error)


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

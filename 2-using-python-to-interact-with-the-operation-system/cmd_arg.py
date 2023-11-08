#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 2:
    print("filename is required!")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("This is a new file.\n")
else:
    print(f"Error, the file {filename} already exists!")
    sys.exit(1)

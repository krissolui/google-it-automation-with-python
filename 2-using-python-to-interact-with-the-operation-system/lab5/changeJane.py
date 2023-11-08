#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]
old_substring = "jane"
new_substring = "jdoe"


with open(filename, "r") as file:
    paths = file.readlines()

for path in paths:
    path = path.strip()
    new_path = path.replace(old_substring, new_substring)
    subprocess.run(["mv", path, new_path])

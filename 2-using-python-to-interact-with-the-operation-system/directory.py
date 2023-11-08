#!/usr/bin/env python3

import os


print("current dir:", os.getcwd())

os.mkdir("new_dir")
os.chdir("new_dir")
os.chdir("..")
os.rmdir("new_dir")
print(os.listdir("."))

dir = "."
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")

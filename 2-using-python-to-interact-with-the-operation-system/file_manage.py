#!/usr/bin/env python3

import os
import datetime

if os.path.exists("example.txt"):
    os.remove("example.txt")

if os.path.exists("original_name.txt"):
    os.rename("original_name.txt", "new_name.txt")

filename = "file_rw.py"
print(f"{filename} exists:", os.path.exists(filename))
print("file size:", os.path.getsize(filename))
ctime = os.path.getctime(filename)
print("ctime:", datetime.datetime.fromtimestamp(ctime))
mtime = os.path.getmtime(filename)
print("mtime:", datetime.datetime.fromtimestamp(mtime))
atime = os.path.getatime(filename)
print("atime:", datetime.datetime.fromtimestamp(atime))
print("absolute path:", os.path.abspath(filename))

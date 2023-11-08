#!/usr/bin/env python3

import os
import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
subprocess.run(["ping", "google.com", "-c", "3"])

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout.decode().split())

result = subprocess.run(
    ["rm", "this_is_a_file_that_does_not_exist.txt"], capture_output=True
)
print(result.returncode)
print(result.stdout)
print(result.stderr)

my_env = os.environ.copy()
my_env = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)

#!/usr/bin/env python3

with open("./health_check.py") as file:
    # for line in file:
    #     print(line.strip())
    rows = file.readlines()
    print(type(rows))
    # for row in rows:
    #     print(row)

with open("./example.txt", "a") as file:
    file.writelines("This is a line. I am a human.")

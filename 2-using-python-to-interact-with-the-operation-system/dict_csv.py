#!/usr/bin/env python3

import csv

filename = "employees.csv"
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {
        "name": "Lio Nelson",
        "username": "lion",
        "department": "User Experience Research",
    },
    {
        "name": "Charlie Grey",
        "username": "greyc",
        "department": "Development",
    },
]

keys = users[0].keys()
with open(filename, "w") as f:
    writer = csv.DictWriter(f=f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(
            "{} 's full name is {}. He/she is in the {} department.".format(
                row["username"], row["name"], row["department"]
            )
        )

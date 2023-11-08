#!/usr/bin/env python3

import csv

filename = "hosts.csv"

hosts = [["workstation.local", "192.168.0.2"], ["webserver.cloud", "10.2.5.6"]]

with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows(hosts)

with open(filename) as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        machine, ip = row
        print(f"Machine: {machine}, IP: {ip}")

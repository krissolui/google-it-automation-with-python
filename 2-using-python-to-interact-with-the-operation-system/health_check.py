#!/usr/bin/env python3

import shutil
import psutil


def check_dist_usage(disk):
    du = shutil.disk_usage(disk)
    free_percentage = du.free / du.total * 100
    return free_percentage > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_dist_usage("/") or not check_cpu_usage():
    print("ERROR!!")
else:
    print("Your machine looks great!")

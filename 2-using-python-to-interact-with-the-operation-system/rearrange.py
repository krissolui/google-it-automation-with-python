#!/usr/bin/env python3

import re


def rearrange_name(name):
    result = re.search(r"^([\w\s\.-]+), ([\w\s\.-]+)$", name)
    if result is None:
        return name

    return f"{result[2]} {result[1]}"

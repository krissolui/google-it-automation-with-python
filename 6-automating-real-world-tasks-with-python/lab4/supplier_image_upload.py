#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
home_path = os.path.expanduser("~")
image_path = os.path.join(home_path, "supplier-data/images")


def main():
    for file in os.scandir(image_path):
        path = file.path
        if file.is_dir() or not path.endswith(".jpeg"):
            continue

        with open(path, "rb") as opened:
            response = requests.post(url, files={"file": opened})

            if response.ok:
                print(f"uploaded image {file}")
            else:
                print(f"failed to upload image {file}")


main()

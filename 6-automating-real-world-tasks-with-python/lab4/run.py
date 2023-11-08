#!/usr/bin/env python3

import os
import requests

server_ip = os.getenv("SERVER_IP", "")
home_path = os.path.expanduser("~")
src_path = os.path.join(home_path, "supplier-data/descriptions")
url = f"http://{server_ip}/fruits/"


def read_file(path: str):
    with open(path) as file:
        lines = file.readlines()
        name, weight, description = lines[0].strip(), lines[1].strip(), lines[2].strip()

        return name, weight, description


def process_data(filename: str, name: str, weight: str, description: str):
    weight = int(weight.replace("lbs", "").strip())
    image = f"{filename.split('.')[0]}.jpeg"
    return name, weight, description, image


def post_request(name: str, weight: int, description: str, image: str):
    data = {
        "name": name,
        "weight": weight,
        "description": description,
        "image_name": image,
    }

    response = requests.post(
        url,
        data=data,
    )
    if response.ok:
        print(f"uploaded fruit {name}")
    else:
        print(f"failed to upload fruit {name}, status code: {response.status_code}")
        print(response.text)


def main():
    for file in os.scandir(src_path):
        if file.is_dir():
            continue
        path = file.path
        name, weight, description = read_file(path)
        name, weight, description, image = process_data(
            file.name, name, weight, description
        )
        # print(name, weight, description, image)
        post_request(name, weight, description, image)


main()

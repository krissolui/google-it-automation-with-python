#!/usr/bin/env python3

import os
import requests

src_path = "/data/feedback"
server_ip = os.environ.get("SERVER_IP", "")
api_url = f"http://{server_ip}/feedback/"


def read_file(path: str):
    with open(path) as file:
        lines = file.readlines()
        title, name, date, feedback = (
            lines[0].strip(),
            lines[1].strip(),
            lines[2].strip(),
            lines[3].strip(),
        )

        return title, name, date, feedback


def post_request(title, name, date, feedback):
    data = {"title": title, "name": name, "date": date, "feedback": feedback}
    response = requests.post(
        api_url,
        data=data,
    )
    if response.ok:
        print(f"request success")
    else:
        print(f"request failed with status code {response.status_code}")


def main():
    files = os.listdir(src_path)

    for file in files:
        path = os.path.join(src_path, file)

        title, name, date, feedback = read_file(path)
        post_request(title, name, date, feedback)


main()

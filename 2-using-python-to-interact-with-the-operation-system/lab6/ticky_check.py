#!/usr/bin/env python3

import csv
import re


# Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (username)
def read_log(log: str):
    result = re.search(r"(ERROR|INFO) ([\w ]+) ", log)
    if result is None:
        return None

    username = re.search(r"\(([\w\.]+)\)", log)
    return result[1], result[2], username[1]


def create_csv(filename: str, data: [dict]):
    keys = data[0].keys()
    with open(filename, "w+") as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(data)


def main():
    log_file = "syslog.log"
    error_count = dict()
    user_stats = dict()

    with open(log_file, "r") as file:
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break

            result = read_log(line)
            if result is None:
                continue

            type, message, username = result

            error_count[message] = error_count.get(message, 0) + 1

            if not username in user_stats:
                user_stats[username] = {"ERROR": 0, "INFO": 0, "count": 0}
            user_stats[username]["count"] = user_stats[username]["count"] + 1
            if type == "ERROR":
                user_stats[username]["ERROR"] += 1
            elif type == "INFO":
                user_stats[username]["INFO"] += 1

    print(error_count)
    print(user_stats)

    create_csv(
        "error_message.csv",
        [
            {"Error": error, "Count": error_count[error]}
            for error in sorted(error_count, key=lambda item: error_count[item])
        ],
    )

    create_csv(
        "user_statistics.csv",
        [
            {
                "Username": username,
                "INFO": user_stats[username]["INFO"],
                "ERROR": user_stats[username]["ERROR"],
            }
            for username in sorted(user_stats)
        ],
    )


if __name__ == "__main__":
    main()

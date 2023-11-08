#!/usr/bin/env python3

import os
import socket
import psutil
from emails import generate_email, send_email

user = os.getenv("USER", "")
sender = "automation@example.com"
recipient = f"{user}@example.com"
body = "Please check your system and resolve the issue as soon as possible."


def check_cpu_usage(max_percent: int = 80) -> bool:
    usage = psutil.cpu_percent(2)
    return usage <= max_percent


def check_disk_space(path: str = "/", min_percent: int = 20) -> bool:
    space = psutil.disk_usage(path)
    free_percent = space.free / space.total * 100
    return free_percent >= min_percent


def check_memory_usage(min_mb: int = 500) -> bool:
    memory = psutil.virtual_memory()
    available_mb = memory.available / 10**6
    return available_mb >= min_mb


def check_localhost(hostname: str = "localhost", ip: str = "127.0.0.1") -> bool:
    try:
        resolved = socket.gethostbyname(hostname)
        return resolved == ip
    except:
        return False


def main():
    checks = [
        (check_cpu_usage, "Error - CPU usage is over 80%"),
        (check_disk_space, "Error - Available disk space is less than 20%"),
        (check_memory_usage, "Error - Available memory is less than 500MB"),
        (check_localhost, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]

    for check, error_message in checks:
        if not check():
            message = generate_email(sender, recipient, error_message, body, None)
            send_email(message)


main()

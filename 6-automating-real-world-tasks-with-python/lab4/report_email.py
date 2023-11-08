#!/usr/bin/env python3

import os
from datetime import datetime
import reports
from emails import generate_email, send_email

user = os.getenv("USER", "")
home_path = os.path.expanduser("~")

src_path = os.path.join(home_path, "supplier-data/descriptions")
report_path = "/tmp/processed.pdf"
date_format = "%B %d, %Y"

sender = "automation@example.com"
recipient = f"{user}@example.com"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."


def read_file(path: str):
    with open(path) as file:
        lines = file.readlines()
        name, weight = lines[0].strip(), lines[1].strip()

        return name, weight


def main():
    now = datetime.now()
    title, paragraph = f"Processed Update on {now.strftime(date_format)}", []

    for file in os.scandir(src_path):
        if file.is_dir():
            continue
        path = file.path
        name, weight = read_file(path)
        paragraph.append(f"name: {name}")
        paragraph.append(f"weight: {weight}")
        paragraph.append("\n")

    reports.generate_report(report_path, title, paragraph)

    email_message = generate_email(sender, recipient, subject, body, report_path)
    send_email(email_message)


main()

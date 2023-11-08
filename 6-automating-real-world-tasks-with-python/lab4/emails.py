#!/usr/bin/env python

import os
import smtplib
import mimetypes
from email.message import EmailMessage
from typing import Optional


email_host = "localhost"


def generate_email(
    sender: str, recipient: str, subject: str, body: str, attachment_path: Optional[str]
):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path is None or attachment_path == "":
        return message

    attachment_name = os.path.basename(attachment_path)
    attachment_type, _ = mimetypes.guess_type(attachment_name)
    maintype, subtype = attachment_type.split("/", 1)
    with open(attachment_path, "rb") as ap:
        message.add_attachment(
            ap.read(), maintype=maintype, subtype=subtype, filename=attachment_name
        )

    return message


def send_email(message: EmailMessage):
    with smtplib.SMTP(email_host) as smtp:
        smtp.send_message(message)

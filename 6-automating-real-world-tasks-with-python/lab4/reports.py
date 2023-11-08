#!/usr/bin/env python3

from typing import List
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment: str, title: str, paragraph: List[str]):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)
    content = [report_title, empty_line]

    for line in paragraph:
        if line == "" or line == "\n":
            content.append(empty_line)
        else:
            report_paragraph = Paragraph(line, styles["BodyText"])
            content.append(report_paragraph)

    report.build(content)

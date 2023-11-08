#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date, data):
    """Returns the employees that started on the given date, or the closest one."""
    date_to_employees = dict()
    # data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if not row_date in date_to_employees:
            date_to_employees[row_date] = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        date_to_employees[row_date].append("{} {}".format(row[0], row[1]))

    return date_to_employees

def list_newer(start_date):
    data = get_file_lines(FILE_URL)
    date_to_employees = get_same_or_newer(start_date, data)
    # while start_date < datetime.datetime.today():
    for start_date in sorted(date_to_employees.keys()):
        # start_date, employees = get_same_or_newer(start_date, data)
        # if not start_date in date_to_employees:
            # continue
        employees = date_to_employees[start_date]
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

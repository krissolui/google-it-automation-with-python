#!/usr/bin/env python3

from enum import Enum

EventType = Enum("EventType", ["login", "logout"])


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


def get_event_date(event: Event):
    return event.date


def join_users_as_str(users: [str]):
    return ", ".join(users)


def print_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            print(f"{machine}: {join_users_as_str(users)}")


def current_users(events: [Event]):
    machines = dict()
    events.sort(key=get_event_date)
    for event in events:
        machine, type, user = event.machine, event.type, event.user
        if machine not in machines:
            machines[machine] = set()
        if type == EventType.login.name:
            machines[machine].add(user)
        elif type == EventType.logout.name and user in machines[machine]:
            machines[machine].remove(user)

    return machines


events = [
    Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "logout", "mailserver.local", "chris"),
]

users = current_users(events)
print(users)
print_report(users)

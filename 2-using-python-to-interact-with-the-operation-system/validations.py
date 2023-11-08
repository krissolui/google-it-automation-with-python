#!/usr/bin/env python3


def validate_username(username, minlen):
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise ValueError("minlen must be positive")

    if len(username) < minlen:
        return False

    if not username.isalnum():
        return False

    return True

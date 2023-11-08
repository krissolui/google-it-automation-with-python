#!/usr/bin/env python3

import re

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "ma")
print(result)

result = re.search(r"^x", "xyz")
print(result)

result = re.search(r"p.ng", "penguin")
print(result)

result = re.search(r"p.ng", "clapping")
print(result)

result = re.search(r"p.ng", "sponge")
print(result)

result = re.search(r"p.ng", "Pangaea", re.IGNORECASE)
print(result)

result = re.search(r"\.com", "welcome")
print(result)

result = re.search(r"\.com", "domain.com")
print(result)

result = re.search(r"A.*a", "Argentina")
print(result)

result = re.search(r"A.*a", "Azerbaijan")
print(result)

result = re.search(r"^A.*a$", "Azerbaijan")
print(result)

result = re.search(r"^A.*a$", "Australia")
print(result)

result = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "_this_is_a_valid_variable_name")
print(result)

result = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "this is not a valid variable")
print(result)

result = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "cream2cake")
print(result)

result = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "1user")
print(result)

result = re.search(r"(\w+), (\w+)", "Jung, Krystal")
print(result.groups())


def rearrange_name(name):
    result = re.search(r"^([\w\s\.-]+), ([\w\s\.-]+)$", name)
    if result is None:
        return name
    else:
        return f"{result[2]} {result[1]}"


print(rearrange_name("Yuan, Yoki"))
print(rearrange_name("Stark, Anthony E."))


def extract_pid(log):
    result = re.search(r"\[(\d+)\]", log)
    if result is None:
        return None
    else:
        return result[1]


print(extract_pid("this is an error made be [12345]. too bad."))

print(extract_pid("someone locked that cat in a [cage]."))

result = re.sub(r"^([\w\s\.-]+), ([\w\s\.-]+)$", r"\2 \1", "Stark, Anthony E.")
print(result)

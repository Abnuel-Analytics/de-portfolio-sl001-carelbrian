"""
Write def normalize(name: str) -> str that trims whitespace and lowercases.
Add three asserts proving it works, including an edge case ("  ABC ").
"""


def normalize(name: str):
    return name.strip().lower()


# Proving it works:
assert normalize("John") == "john"
assert normalize(" hElLo ") == "hello"
assert normalize(" ABC ") == "abc"

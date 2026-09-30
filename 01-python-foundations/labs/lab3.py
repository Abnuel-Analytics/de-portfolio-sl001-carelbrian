"""
Write a function that takes a list of dicts and writes them to out.jsonl
(one JSON object per line), then a function that reads them back into a
list. Prove round-trip equality.
"""

import json


def write_jsonl(data, filepath):
    # 'w' means "open this file for writing" (creates it if it doesn't exist)
    with open(filepath, "w") as f:
        for row in data:
            # 1. Translate dict to text string
            text_version = json.dumps(row)

            # 2. Write the text, PLUS a newline character (\n) to hit "Enter"
            f.write(text_version + "\n")


def read_jsonl(filepath):
    result = []

    # 'r' means "open this file for reading"
    with open(filepath, "r") as f:
        # .readlines() automatically splits the file into a list of strings by line
        for line in f:
            # Translate text string back to dict
            python_dict = json.loads(line)

            # Add it to our list
            result.append(python_dict)

    return result


# 1. Our original data
original_data = [{"id": 1, "amt": 10}, {"id": 2, "amt": 30}, {"id": 1, "amt": 5}]

# 2. Send it on the round-trip
write_jsonl(original_data, "out.jsonl")
returned_data = read_jsonl("out.jsonl")

# 3. The assert
assert original_data == returned_data

print("Round-trip successful check your folder for out.jsonl")

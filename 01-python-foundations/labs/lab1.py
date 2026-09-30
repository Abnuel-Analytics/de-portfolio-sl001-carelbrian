""" "
Given rows = [{"id":1, "amt":10}, {"id":2, "amt":30}, {"id":1, "amt":5}]
Build a set of unique ids
Do (1) again as a one-line where possible
"""

rows = [{"id": 1, "amt": 10}, {"id": 2, "amt": 30}, {"id": 1, "amt": 5}]

# 1 - Build a dict mapping each id to the sum of its amt.
totals = {}

for row in rows:
    current_id = row["id"]
    current_amt = row["amt"]

    if current_id in totals:
        # If we've seen them before, add to the existing total
        totals[current_id] = totals[current_id] + current_amt
    else:
        # If it's the first time seeing them, create the entry
        totals[current_id] = current_amt

print(totals)

# 2 - Build a set of unique ids
unique_ids = set()

for row in rows:
    unique_ids.add(row["id"])

print(unique_ids)


# 3 - Do task 1 again as a one-liner where possible
from collections import defaultdict  # noqa: E402

# This creates a dictonary that defaults missing key to 0
totals = defaultdict(int)

for row in rows:
    totals[row["id"]] += row["amt"]

print(totals)

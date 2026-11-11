# Nested comprehensions — several "for" clauses, read LEFT TO RIGHT
# exactly like nested loops written top to bottom:
#
#   [expr for a in A for b in B]   ==   for a in A:
#                                           for b in B:
#                                               result.append(expr)

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: flatten all items of all orders into one list
orders = [
    {"id": 1, "items": ["keyboard", "mouse"]},
    {"id": 2, "items": ["monitor"]},
    {"id": 3, "items": ["cable", "adapter", "mouse"]},
]

# --- BEFORE: nested for loops -----------------------------------------------
all_items = []
for order in orders:
    for item in order["items"]:
        all_items.append(item)

print(all_items)

# --- AFTER: nested comprehension --------------------------------------------
all_items = [item for order in orders for item in order["items"]]
print(all_items)


# --- More examples ----------------------------------------------------------

# all combinations: product variants for an online shop
sizes = ["S", "M", "L"]
colors = ["black", "white"]
print([f"T-shirt {size}/{color}" for size in sizes for color in colors])

# a comprehension INSIDE a comprehension: parse a CSV into a list of rows
csv_text = "1,2,3\n4,5,6\n7,8,9"
matrix = [[int(cell) for cell in line.split(",")] for line in csv_text.splitlines()]
print(matrix)

# transpose rows <-> columns
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])

# time slots for a booking calendar
days = ["Mon", "Tue"]
hours = range(9, 12)
print([f"{day} {hour}:00" for day in days for hour in hours])

# Tip: two levels is the limit for readability. Deeper — use regular loops.


# --- With employees.json ----------------------------------------------------

# all words from the first 3 job titles, in one flat list
titles = [e["job_title"] for e in employees[:3]]
print([word for title in titles for word in title.split()])

# pair each Ukrainian employee with each Japanese one (e.g. for a mentoring exchange)
ua = [e["first_name"] for e in employees if e["iso_code"] == "UA"]
jp = [e["first_name"] for e in employees if e["iso_code"] == "JP"]
pairs = [(u, j) for u in ua for j in jp]
print(f"{len(pairs)} pairs, e.g. {pairs[:3]}")

# salary table: rows = shirt size, columns = salaries of people with that size
sizes = ["XS", "S", "M"]
table = [[e["annual_salary"] for e in employees if e["shirt_size"] == size] for size in sizes]
for size, salaries in zip(sizes, table):
    print(size, len(salaries), "employees")

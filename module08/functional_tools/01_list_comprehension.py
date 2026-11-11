# list comprehension — build a new list from an iterable in one expression
# syntax: [expression for item in iterable]

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: convert prices from strings (as they come from a CSV/form) to floats
raw_prices = ["19.99", "5.50", "120.00", "3.25"]

# --- BEFORE: for loop + append ----------------------------------------------
prices = []
for raw in raw_prices:
    prices.append(float(raw))

print(prices)

# --- AFTER: list comprehension ----------------------------------------------
prices = [float(raw) for raw in raw_prices]
print(prices)


# --- More examples ----------------------------------------------------------

# clean user-entered tags
tags = ["  Python", "DJANGO ", " web dev "]
print([tag.strip().lower().replace(" ", "-") for tag in tags])

# build file paths for a batch of reports
months = ["2026-01", "2026-02", "2026-03"]
print([f"reports/sales_{month}.csv" for month in months])

# extract one field from a list of dicts (a very common pattern)
orders = [
    {"id": 101, "total": 59.90},
    {"id": 102, "total": 15.00},
    {"id": 103, "total": 240.10},
]
order_ids = [order["id"] for order in orders]
print(order_ids)

# call a method on every object: word lengths for a text statistic
sentence = "Comprehensions make simple transformations short and readable"
print([len(word) for word in sentence.split()])


# --- With employees.json ----------------------------------------------------

# full names for an email "To:" list
print([f"{e['first_name']} {e['last_name']} <{e['email']}>" for e in employees[:3]])

# monthly salary for every employee
monthly = [round(e["annual_salary"] / 12, 2) for e in employees]
print(monthly[:5])

# usernames from the part before "@"
print([e["email"].split("@")[0] for e in employees[:5]])

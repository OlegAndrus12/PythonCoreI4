# Conditions inside comprehensions — two different things!
#
#   [x for x in items if condition]          -> FILTER: keeps some items
#   [a if condition else b for x in items]   -> TRANSFORM: every item stays,
#                                               value depends on condition

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: keep only paid orders
orders = [
    {"id": 1, "total": 50.0, "paid": True},
    {"id": 2, "total": 75.5, "paid": False},
    {"id": 3, "total": 20.0, "paid": True},
]

# --- BEFORE: for loop + if --------------------------------------------------
paid_ids = []
for order in orders:
    if order["paid"]:
        paid_ids.append(order["id"])

print(paid_ids)

# --- AFTER: comprehension with a filter -------------------------------------
paid_ids = [order["id"] for order in orders if order["paid"]]
print(paid_ids)


# Task: label every order (nothing is removed)

# --- BEFORE: for loop + if/else ---------------------------------------------
labels = []
for order in orders:
    if order["paid"]:
        labels.append("PAID")
    else:
        labels.append("PENDING")

print(labels)

# --- AFTER: comprehension with a conditional expression ---------------------
labels = ["PAID" if order["paid"] else "PENDING" for order in orders]
print(labels)


# --- More examples ----------------------------------------------------------

# keep only lines that are not comments or blank (e.g. reading a .env file)
env_file = """\
# database settings
DB_HOST=localhost

DB_PORT=5432
# DEBUG=true
"""
settings = [line for line in env_file.splitlines() if line and not line.startswith("#")]
print(settings)

# replace missing values with a default
ratings = [4.5, None, 3.0, None, 5.0]
print([r if r is not None else 0 for r in ratings])

# filter AND transform: apply a 10% discount only to items above 100
cart = [30, 150, 80, 220]
print([round(price * 0.9, 2) if price > 100 else price for price in cart])

# several conditions
words = ["api", "Python", "rest", "Django", "sql", "Flask"]
print([w for w in words if w[0].isupper() if len(w) > 5])  # two ifs == and


# --- With employees.json ----------------------------------------------------

# emails of employees with no shirt size (filter)
print([e["email"] for e in employees if not e["shirt_size"]][:5])

# seniority level for everyone (transform with if/else)
levels = [
    "senior" if e["years_of_experience"] >= 7 else "middle" if e["years_of_experience"] >= 4 else "junior"
    for e in employees
]
print(levels[:10])

# high earners in China, by name (filter + transform)
print([e["first_name"] for e in employees if e["iso_code"] == "CN" and e["annual_salary"] > 150_000])

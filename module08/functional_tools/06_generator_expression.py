# generator expression — a LAZY comprehension
# syntax: (expression for item in iterable if condition)
#
# It does not build a list in memory; values are produced one by one on demand.
# Perfect for feeding sum(), max(), any(), all(), "".join() or big files.
# A generator can be consumed only ONCE.

import json
import sys
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: total of a shopping cart

cart = [
    {"item": "book", "price": 12.5, "qty": 2},
    {"item": "pen", "price": 1.2, "qty": 10},
    {"item": "bag", "price": 35.0, "qty": 1},
]

# --- BEFORE: for loop with an accumulator ------------------------------------
total = 0
for line in cart:
    total += line["price"] * line["qty"]

print(total)

# --- AFTER: generator expression fed into sum() -----------------------------
total = sum(line["price"] * line["qty"] for line in cart)  # no extra () needed
print(total)


# --- More examples ----------------------------------------------------------

# memory: a list stores all values, a generator stores only "how to get the next"
as_list = [n * n for n in range(1_000_000)]
as_gen = (n * n for n in range(1_000_000))
print(f"list: {sys.getsizeof(as_list):,} bytes, generator: {sys.getsizeof(as_gen)} bytes")

# a generator is consumed only once!
gen = (n for n in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] — already exhausted

# process a "huge" log lazily: count errors without loading everything into a list
log_lines = (f"line {i} {'ERROR' if i % 1000 == 0 else 'INFO'}" for i in range(100_000))
print(sum(1 for line in log_lines if "ERROR" in line))

# build a string
words = ["functional", "programming", "in", "python"]
print(" ".join(word.capitalize() for word in words))

# stop early: next() returns the FIRST match, the rest is never computed
users = [{"name": "alice", "admin": False}, {"name": "bob", "admin": True}]
first_admin = next((u for u in users if u["admin"]), None)
print(first_admin)


# --- With employees.json ----------------------------------------------------

# average salary without building an intermediate list
average = sum(e["annual_salary"] for e in employees) / len(employees)
print(f"Average salary: {average:,.2f}")

# the oldest employee's age
print(f"Oldest: {max(e['age'] for e in employees)}")

# first employee from Japan (or None if there is none)
first_jp = next((e for e in employees if e["iso_code"] == "JP"), None)
print(first_jp["first_name"], first_jp["last_name"])

# CSV export, row by row, without keeping all rows in memory
header = "id,name,salary"
rows = (f"{e['id']},{e['first_name']} {e['last_name']},{e['annual_salary']}" for e in employees)
csv_text = "\n".join([header, *rows])
print(csv_text[:120], "...")

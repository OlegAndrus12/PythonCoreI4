# zip(*iterables) — pair up elements by position, stops at the SHORTEST iterable

import json
from itertools import zip_longest
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: turn CSV rows into dicts using the header row
header = ["id", "name", "email"]
rows = [
    ["1", "Alice", "alice@mail.com"],
    ["2", "Bob", "bob@mail.com"],
]

# --- BEFORE: loop over indexes ----------------------------------------------
users = []
for row in rows:
    user = {}
    for i in range(len(header)):
        user[header[i]] = row[i]
    users.append(user)

print(users)

# --- AFTER: zip -------------------------------------------------------------
users = [dict(zip(header, row)) for row in rows]
print(users)


# --- More examples ----------------------------------------------------------

# print a receipt: walk two lists in parallel
items = ["coffee", "croissant", "juice"]
prices = [2.50, 3.20, 4.00]
for item, price in zip(items, prices):
    print(f"{item:<12}{price:>6.2f}")

# day-to-day change of a stock price: pair each value with the next one
closing_prices = [101.5, 103.0, 99.8, 104.2, 104.2]
changes = [round(today - yesterday, 2) for yesterday, today in zip(closing_prices, closing_prices[1:])]
print(changes)

# column totals of a sales table: zip(*rows) "transposes" rows into columns
monthly_sales = [
    # Jan, Feb, Mar
    [120, 135, 150],  # shop A
    [90, 110, 95],    # shop B
    [200, 180, 210],  # shop C
]
print([sum(month) for month in zip(*monthly_sales)])

# compare expected vs actual test results
expected = [4, 9, 16, 25]
actual = [4, 9, 15, 25]
for i, (exp, act) in enumerate(zip(expected, actual)):
    if exp != act:
        print(f"test #{i} failed: expected {exp}, got {act}")

# zip stops silently at the shortest list — zip_longest shows the gap
team = ["Alice", "Bob", "Charlie"]
tasks = ["review PR", "write tests"]
print(list(zip(team, tasks)))                                # Charlie is lost!
print(list(zip_longest(team, tasks, fillvalue="(no task)")))


# --- With employees.json ----------------------------------------------------

# a quick lookup table: id -> email
ids = [e["id"] for e in employees]
emails = [e["email"] for e in employees]
email_by_id = dict(zip(ids, emails))
print(email_by_id[42])

# apply a list of new salaries (e.g. from a spreadsheet) to the first employees
new_salaries = [190_000, 200_000, 105_000]
for emp, new_salary in zip(employees, new_salaries):
    diff = new_salary - emp["annual_salary"]
    print(f"{emp['first_name']:<10} {emp['annual_salary']:>10.2f} -> {new_salary:>10} ({diff:+.2f})")

# "unzip" (name, salary) pairs into two separate tuples for a chart
pairs = [(e["first_name"], e["annual_salary"]) for e in employees[:5]]
names, salaries = zip(*pairs)
print(names)
print(salaries)

# who gets paid more than the colleague listed next?
for current, nxt in zip(employees[:5], employees[1:6]):
    if current["annual_salary"] > nxt["annual_salary"]:
        print(f"{current['first_name']} earns more than {nxt['first_name']}")

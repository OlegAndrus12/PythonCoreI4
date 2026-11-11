# functools.reduce(func, iterable, initial) — fold a sequence into ONE value
# func(accumulator, item) -> new accumulator

import json
from functools import reduce
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: total years of experience across all employees

# --- BEFORE: plain for loop -------------------------------------------------
total_years = 0
for emp in employees:
    total_years += emp["years_of_experience"]

print(total_years)

# --- AFTER: reduce ----------------------------------------------------------
total_years = reduce(lambda acc, emp: acc + emp["years_of_experience"], employees, 0)
print(total_years)

# NOTE: for simple sums, the built-in sum() is the most readable option
print(sum(emp["years_of_experience"] for emp in employees))


# --- More examples ----------------------------------------------------------

# merge config layers: defaults <- config file <- environment overrides
defaults = {"host": "localhost", "port": 8000, "debug": False}
from_file = {"port": 8080, "db": "app.sqlite"}
from_env = {"debug": True}

config = reduce(lambda merged, layer: {**merged, **layer}, [defaults, from_file, from_env])
print(config)

# read a nested value by a dotted path: "database.credentials.user"
settings = {"database": {"credentials": {"user": "admin", "password": "secret"}}}
user = reduce(lambda node, key: node[key], "database.credentials.user".split("."), settings)
print(user)

# build a processing pipeline from small functions
steps = [str.strip, str.lower, lambda s: s.replace(" ", "-")]
slug = reduce(lambda value, step: step(value), steps, "  Hello World From Python  ")
print(slug)


# count employees per shirt size — the accumulator is a dict
def count_by_size(acc, emp):
    size = emp["shirt_size"] or "unknown"
    acc[size] = acc.get(size, 0) + 1
    return acc


print(reduce(count_by_size, employees, {}))


# --- With employees.json ----------------------------------------------------

# total payroll
payroll = reduce(lambda acc, e: acc + e["annual_salary"], employees, 0)
print(f"Total payroll: {payroll:,.2f}")

# the highest-paid employee (the same as max(employees, key=...))
top = reduce(lambda best, e: e if e["annual_salary"] > best["annual_salary"] else best, employees)
print(f"Highest paid: {top['first_name']} {top['last_name']} — {top['annual_salary']}")

# youngest and oldest age in ONE pass: the accumulator is a tuple
youngest, oldest = reduce(
    lambda acc, e: (min(acc[0], e["age"]), max(acc[1], e["age"])),
    employees,
    (float("inf"), float("-inf")),
)
print(f"Ages from {youngest} to {oldest}")

# index employees by country: {"UA": ["Name", ...], ...}
def group_by_country(acc, e):
    acc.setdefault(e["iso_code"], []).append(e["first_name"])
    return acc


by_country = reduce(group_by_country, employees, {})
print(by_country["UA"])

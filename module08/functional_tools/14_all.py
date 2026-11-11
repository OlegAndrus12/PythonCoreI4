# all(iterable) — True only if EVERY element is truthy
# short-circuits: stops at the first False. all([]) is True.

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: a strong password has an uppercase letter, a lowercase letter,
# a digit and is at least 8 characters long


# --- BEFORE: loops and flags ------------------------------------------------
def validate_password_loop(password):
    has_upper = False
    has_lower = False
    has_digit = False
    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit and len(password) >= 8


print(validate_password_loop("Secure1!"))
print(validate_password_loop("weakpass"))
print(validate_password_loop("NOLOWER1"))


# --- AFTER: all + any -------------------------------------------------------
def validate_password(password):
    rules = [
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        len(password) >= 8,
    ]
    return all(rules)


print(validate_password("Secure1!"))
print(validate_password("weakpass"))
print(validate_password("NOLOWER1"))


# --- More examples ----------------------------------------------------------

# a sign-up form is complete only if every required field is filled
form = {"name": "Alice", "email": "alice@mail.com", "phone": ""}
required = ["name", "email", "phone"]
if not all(form.get(field) for field in required):
    missing = [field for field in required if not form.get(field)]
    print(f"Please fill in: {', '.join(missing)}")

# check a CSV file has all the columns we need before importing it
csv_header = "id,first_name,last_name,email,age".split(",")
needed = ["id", "email", "age"]
print(f"Can import: {all(col in csv_header for col in needed)}")

# role-based access: user must have every permission the action requires
user_perms = {"read", "write"}
delete_requires = {"read", "write", "delete"}
print(f"Can delete: {all(p in user_perms for p in delete_requires)}")

# deploy only if every CI check passed
ci_checks = {"lint": "passed", "tests": "passed", "build": "failed"}
if all(result == "passed" for result in ci_checks.values()):
    print("Deploying...")
else:
    print("Deploy blocked by failing checks")

# sanity check: are the log timestamps in chronological order?
timestamps = ["09:00:01", "09:00:05", "09:01:12", "09:00:59"]
in_order = all(a <= b for a, b in zip(timestamps, timestamps[1:]))
print(f"Timestamps in order: {in_order}")


# --- With employees.json ----------------------------------------------------

# data-quality checks before importing the file into a database
checks = {
    "all adults": all(e["age"] >= 18 for e in employees),
    "all emails contain @": all("@" in e["email"] for e in employees),
    "all ids unique": len({e["id"] for e in employees}) == len(employees),
    "all salaries positive": all(e["annual_salary"] > 0 for e in employees),
    "all shirt sizes filled": all(e["shirt_size"] for e in employees),
}
for check, ok in checks.items():
    print(f"{'OK  ' if ok else 'FAIL'} {check}")

# does every record have all the required fields?
required_fields = ["id", "first_name", "last_name", "email", "annual_salary"]
print(f"Schema OK: {all(all(f in e for f in required_fields) for e in employees)}")

# is the file sorted by id?
print(f"Sorted by id: {all(a['id'] < b['id'] for a, b in zip(employees, employees[1:]))}")

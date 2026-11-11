# map(func, iterable, ...) — apply func to every element, returns a lazy iterator

import json
from pathlib import Path

# Our company has grown so fast this year, so every employee with at least
# five years of experience gets a raise according to this table:
#    5 years: 5%,  6 years: 7.5%,  7 years: 10%,
#    8 years: 12.5%,  9 years: 15%,  10 years: 20%
BONUS_SCALE = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1.05,
    6: 1.075,
    7: 1.1,
    8: 1.125,
    9: 1.15,
    10: 1.2,
}

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# --- BEFORE: plain for loop -------------------------------------------------
salaries_with_bonus = []
for emp in employees:
    multiplier = BONUS_SCALE[emp["years_of_experience"]]
    salaries_with_bonus.append(round(emp["annual_salary"] * multiplier, 2))

print(salaries_with_bonus[:5])


# --- AFTER: map -------------------------------------------------------------
def salary_with_bonus(emp):
    multiplier = BONUS_SCALE[emp["years_of_experience"]]
    return round(emp["annual_salary"] * multiplier, 2)


salaries_with_bonus = list(map(salary_with_bonus, employees))
print(salaries_with_bonus[:5])


# --- More examples ----------------------------------------------------------

# parse numbers from user input / a CSV line
user_input = "10 20 35 5"  # e.g. input("Enter numbers: ")
numbers = list(map(int, user_input.split()))
print(f"sum={sum(numbers)}, max={max(numbers)}")

csv_line = "2026-11-10,19.99,3,4.5"
date, price, qty, rating = csv_line.split(",")
price, rating = map(float, (price, rating))
print(date, price, int(qty), rating)

# normalize emails before saving them to a database
raw_emails = ["  Alice@Mail.com", "BOB@mail.COM ", " carol@mail.com"]
emails = list(map(lambda e: e.strip().lower(), raw_emails))
print(emails)

# invoice lines: map over two lists at once — price * quantity
prices = [10.0, 25.5, 8.99]
quantities = [3, 1, 5]
line_totals = list(map(lambda p, q: round(p * q, 2), prices, quantities))
print(f"lines={line_totals}, total={sum(line_totals):.2f}")

# add VAT to every price in a price list
VAT = 0.20
price_list = {"coffee": 2.50, "tea": 2.00, "cake": 3.75}
with_vat = dict(map(lambda item: (item[0], round(item[1] * (1 + VAT), 2)), price_list.items()))
print(with_vat)


# --- With employees.json ----------------------------------------------------

# full names for a badge printer
full_names = list(map(lambda e: f"{e['first_name']} {e['last_name']}", employees))
print(full_names[:5])

# monthly salary for the payroll export
monthly = list(map(lambda e: round(e["annual_salary"] / 12, 2), employees))
print(monthly[:5])

# email domains used by employees
domains = set(map(lambda e: e["email"].split("@")[1], employees))
print(f"{len(domains)} distinct domains, e.g. {sorted(domains)[:3]}")

# a lightweight "public profile" — keep only the fields an API should expose
public = list(map(lambda e: {"id": e["id"], "name": e["first_name"], "job": e["job_title"]}, employees))
print(public[:2])

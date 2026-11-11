# dict comprehension — build a dict in one expression
# syntax: {key_expr: value_expr for item in iterable if condition}

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

games = {
    "The Legend of Zelda: Ocarina of Time": 1998,
    "Grand Theft Auto IV": 2008,
    "Red Dead Redemption": 2010,
    "Perfect Dark": 2000,
    "The Orange Box": 2007,
}

# Task: keep only games released after 2000

# --- BEFORE: for loop -------------------------------------------------------
modern_games = {}
for title, year in games.items():
    if year > 2000:
        modern_games[title] = year

print(modern_games)

# --- AFTER: dict comprehension ----------------------------------------------
modern_games = {title: year for title, year in games.items() if year > 2000}
print(modern_games)


# --- More examples ----------------------------------------------------------

# lowercase keys (e.g. normalize HTTP headers)
headers = {"Content-Type": "application/json", "X-Request-ID": "abc123"}
print({name.lower(): value for name, value in headers.items()})

# games released in a range of years
print({title: year for title, year in games.items() if 2000 <= year <= 2008})

# invert a dict: value -> key (country code -> country name)
countries = {"Ukraine": "UA", "Japan": "JP", "China": "CN"}
code_to_country = {code: name for name, code in countries.items()}
print(code_to_country["JP"])

# apply a price change to a whole price list
prices = {"coffee": 2.50, "tea": 2.00, "cake": 3.75}
print({item: round(price * 1.1, 2) for item, price in prices.items()})

# parse a query string: "page=2&sort=price&order=desc"
query = "page=2&sort=price&order=desc"
params = {key: value for key, value in (pair.split("=") for pair in query.split("&"))}
print(params)

# drop empty values from a form before saving it
form = {"name": "Alice", "phone": "", "email": "alice@mail.com", "company": None}
print({k: v for k, v in form.items() if v})


# --- With employees.json ----------------------------------------------------

# lookup table: id -> full employee record (fast access by id)
by_id = {e["id"]: e for e in employees}
print(by_id[42]["first_name"], by_id[42]["job_title"])

# email -> annual salary
salary_by_email = {e["email"]: e["annual_salary"] for e in employees}
print(list(salary_by_email.items())[:3])

# number of employees per country
codes = [e["iso_code"] for e in employees]
per_country = {code: codes.count(code) for code in set(codes)}
print(sorted(per_country.items(), key=lambda item: item[1], reverse=True)[:5])

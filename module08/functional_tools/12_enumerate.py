# enumerate(iterable, start=0) — yields (index, element) pairs

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: show a numbered menu to the user
menu = ["New game", "Load game", "Settings", "Exit"]

# --- BEFORE: manual counter -------------------------------------------------
number = 1
for option in menu:
    print(f"{number}. {option}")
    number += 1

# --- AFTER: enumerate -------------------------------------------------------
for number, option in enumerate(menu, start=1):
    print(f"{number}. {option}")

choice = 3  # e.g. int(input("Choose: "))
print(f"You chose: {menu[choice - 1]}")


# --- More examples ----------------------------------------------------------

# report line numbers of invalid lines in a config file
config_text = """\
host=localhost
port=8080
debug
timeout=30
=oops
"""
for line_no, line in enumerate(config_text.splitlines(), start=1):
    key, sep, value = line.partition("=")
    if not sep or not key or not value:
        print(f"config line {line_no}: invalid entry {line!r}")

# leaderboard: rank players after sorting by score
scores = {"alice": 320, "bob": 450, "carol": 380}
ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)
for place, (player, score) in enumerate(ranking, start=1):
    print(f"#{place} {player:<6} {score}")

# process data in batches and show progress
records = list(range(1, 11))
BATCH = 4
for batch_no, start in enumerate(range(0, len(records), BATCH), start=1):
    print(f"batch {batch_no}: {records[start:start + BATCH]}")


# --- With employees.json ----------------------------------------------------

# top-5 earners leaderboard
top5 = sorted(employees, key=lambda e: e["annual_salary"], reverse=True)[:5]
for place, e in enumerate(top5, start=1):
    full_name = f"{e['first_name']} {e['last_name']}"
    print(f"#{place} {full_name:<25} {e['annual_salary']:>12,.2f}")

# numbered "to contact" list: people who still need to give a shirt size
no_size = [e for e in employees if not e["shirt_size"]]
for n, e in enumerate(no_size[:5], start=1):
    print(f"{n}. {e['first_name']} {e['last_name']} <{e['email']}>")

# data validation: report the record POSITION (not id) of suspicious rows
for index, e in enumerate(employees):
    if e["years_of_experience"] > e["age"] - 16:
        print(f"record {index}: {e['age']} years old with {e['years_of_experience']} years of experience?")

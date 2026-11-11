# filter(predicate, iterable) — keep only elements for which predicate is truthy
# returns a lazy iterator

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: employees with at most 3 years of experience AND at most 25 years old

# --- BEFORE: plain for loop -------------------------------------------------
young_juniors = []
for emp in employees:
    if emp["years_of_experience"] <= 3 and emp["age"] <= 25:
        young_juniors.append(emp)

print(f"Young juniors: {len(young_juniors)}")

# --- AFTER: filter ----------------------------------------------------------
young_juniors = list(
    filter(lambda emp: emp["years_of_experience"] <= 3 and emp["age"] <= 25, employees)
)
print(f"Young juniors: {len(young_juniors)}")


# --- More examples ----------------------------------------------------------

# employees without a shirt size — who do we need to ask before ordering merch?
no_shirt_size = list(filter(lambda emp: not emp["shirt_size"], employees))
print(f"Employees with no shirt size: {len(no_shirt_size)}")

# pull only errors out of a log
log = """\
2026-11-10 09:00:01 INFO  server started
2026-11-10 09:00:05 ERROR database connection refused
2026-11-10 09:01:12 INFO  user alice logged in
2026-11-10 09:02:40 ERROR payment gateway timeout
"""
errors = list(filter(lambda line: " ERROR " in line, log.splitlines()))
print(*errors, sep="\n")

# drop blank lines: filter(None, ...) keeps only truthy values ("" is falsy)
text = "first line\n\n   \nsecond line\n\nthird line\n"
lines = list(filter(None, map(str.strip, text.splitlines())))
print(lines)

# pick only image files from an upload
uploads = ["cat.jpg", "report.pdf", "logo.PNG", "notes.txt", "photo.jpeg"]
images = list(filter(lambda f: f.lower().endswith((".jpg", ".jpeg", ".png")), uploads))
print(images)

# a named predicate reads best — filter shines here
def is_valid_email(email):
    name, _, domain = email.partition("@")
    return bool(name) and "." in domain


emails = ["alice@mail.com", "not-an-email", "bob@mail.com", "broken@", "carol@mail.com"]
print(list(filter(is_valid_email, emails)))

# chaining map + filter: orders worth more than 100 after a 10% discount
orders = [120, 80, 250, 95, 110]
big_orders = filter(lambda total: total > 100, map(lambda total: total * 0.9, orders))
print(list(big_orders))


# --- With employees.json ----------------------------------------------------

# employees based in Ukraine
ukraine = list(filter(lambda e: e["iso_code"] == "UA", employees))
print([f"{e['first_name']} {e['last_name']}" for e in ukraine])

# everyone with "Engineer" in their job title
engineers = list(filter(lambda e: "Engineer" in e["job_title"], employees))
print(f"Engineers: {len(engineers)}")

# employees earning above the company average
average = sum(e["annual_salary"] for e in employees) / len(employees)
above_average = list(filter(lambda e: e["annual_salary"] > average, employees))
print(f"Average salary {average:.2f}; {len(above_average)} people earn more")

# candidates for a mentoring program: 8+ years of experience, 40+ years old
mentors = list(filter(lambda e: e["years_of_experience"] >= 8 and e["age"] >= 40, employees))
print(f"Potential mentors: {len(mentors)}")

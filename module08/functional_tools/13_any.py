# any(iterable) — True if AT LEAST ONE element is truthy
# short-circuits: stops at the first True. any([]) is False.

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)


def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']}")


applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": True,
    },
]

# Task: invite a candidate who meets AT LEAST ONE of the criteria:
# knows Python, has 5+ years of experience, or has a degree

# --- BEFORE: loop with a flag -----------------------------------------------
for applicant in applicants:
    criteria = [
        "python" in applicant["programming_languages"],
        applicant["years_of_experience"] >= 5,
        applicant["has_degree"],
    ]
    qualifies = False
    for criterion in criteria:
        if criterion:
            qualifies = True
            break
    if qualifies:
        schedule_interview(applicant)

# --- AFTER: any -------------------------------------------------------------
for applicant in applicants:
    criteria = [
        "python" in applicant["programming_languages"],
        applicant["years_of_experience"] >= 5,
        applicant["has_degree"],
    ]
    if any(criteria):
        schedule_interview(applicant)


# --- More examples ----------------------------------------------------------

# block an upload that contains a dangerous file type
uploads = ["photo.jpg", "invoice.pdf", "setup.EXE"]
blocked = (".exe", ".bat", ".sh")
if any(name.lower().endswith(blocked) for name in uploads):
    print("Upload rejected: executable files are not allowed")

# moderate a comment
banned_words = {"spam", "scam", "casino"}
comment = "Win big at our online casino today!"
if any(word.strip("!.,").lower() in banned_words for word in comment.split()):
    print("Comment sent to moderation")

# can we ship the order? not if any item is out of stock
cart = [
    {"item": "book", "in_stock": True},
    {"item": "pen", "in_stock": False},
    {"item": "notebook", "in_stock": True},
]
if any(not line["in_stock"] for line in cart):
    print("Some items are out of stock — order is on hold")

# alert if any server is unhealthy
health = {"web-1": "ok", "web-2": "ok", "db-1": "down"}
if any(status != "ok" for status in health.values()):
    print("ALERT: at least one service is down")

# Tip: pass a generator, not a list — any([...]) builds the whole list first
# and loses the short-circuit benefit.


# --- With employees.json ----------------------------------------------------

# do we have anyone under 21? (e.g. for a company event with alcohol)
print(f"Anyone under 21: {any(e['age'] < 21 for e in employees)}")

# do we have any employee in Ukraine?
print(f"Anyone in UA: {any(e['iso_code'] == 'UA' for e in employees)}")

# is anyone paid more than 240 000?
print(f"Anyone above 240k: {any(e['annual_salary'] > 240_000 for e in employees)}")

# can we order merch yet? not if any shirt size is missing
if any(not e["shirt_size"] for e in employees):
    print("Merch order on hold: some shirt sizes are missing")

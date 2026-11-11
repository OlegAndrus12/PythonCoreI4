# set comprehension — like a list comprehension, but with {} and NO duplicates
# syntax: {expression for item in iterable if condition}
# Note: {} alone is an empty DICT; an empty set is set().

import json
from pathlib import Path

with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

# Task: which unique pages did visitors open? (from an access log)
visits = [
    "/home", "/products", "/home", "/cart", "/products", "/checkout", "/home",
]

# --- BEFORE: for loop + set.add ---------------------------------------------
unique_pages = set()
for page in visits:
    unique_pages.add(page)

print(unique_pages)

# --- AFTER: set comprehension -----------------------------------------------
unique_pages = {page for page in visits}  # same as set(visits)
print(unique_pages)


# --- More examples ----------------------------------------------------------

# unique, case-insensitive email addresses (deduplicate a mailing list)
subscribers = ["Alice@Mail.com", "bob@mail.com", "alice@mail.com", "BOB@MAIL.COM"]
print({email.lower() for email in subscribers})

# which file types were uploaded?
uploads = ["cat.jpg", "report.pdf", "photo.JPG", "notes.txt", "scan.pdf"]
print({name.rsplit(".", 1)[-1].lower() for name in uploads})

# unique hashtags in a list of posts
posts = ["Learning #python today", "#Python and #django", "Weekend #coding"]
print({word.lower() for post in posts for word in post.split() if word.startswith("#")})

# set operations after a set comprehension: who has NOT submitted homework?
students = {"alice", "bob", "carol", "dave"}
submissions = ["alice_hw1.py", "carol_hw1.py"]
submitted = {name.split("_")[0] for name in submissions}
print(students - submitted)


# --- With employees.json ----------------------------------------------------

# countries the company operates in
countries = {e["iso_code"] for e in employees}
print(f"{len(countries)} countries")

# shirt sizes to order (no empty values)
print({e["shirt_size"] for e in employees if e["shirt_size"]})

# how many emails share a domain with someone else?
domains = [e["email"].split("@")[1] for e in employees]
print(f"{len(domains)} emails, {len({d for d in domains})} unique domains")

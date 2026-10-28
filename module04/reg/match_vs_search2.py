import re

# re.match  — anchored to the START of the string
# re.search — scans the ENTIRE string, returns first match anywhere

log = "ERROR 500: database connection lost"

# 'ERROR' is at the start → both find it
print(re.match(r"ERROR", log))    # <Match ...>
print(re.search(r"ERROR", log))   # <Match ...>

print()

# '500' is in the middle → only search finds it
print(re.match(r"500", log))      # None  ← match gives up immediately
print(re.search(r"500", log))     # <Match '500' span=(6, 9)>

print()

# --- Practical difference ---

logs = [
    "ERROR 500: database connection lost",
    "WARNING: disk usage at 91%",
    "INFO: server started on port 8000",
    "ERROR 404: page not found",
]

print("Lines that START with ERROR (match):")
for line in logs:
    if re.match(r"ERROR", line):
        print(" ", line)

print()

print("Lines that CONTAIN '500' anywhere (search):")
for line in logs:
    if re.search(r"\b500\b", line):
        print(" ", line)

print()

# --- When to use which ---
# match  → validate format/prefix: log level, file path prefix, protocol
# search → find a pattern anywhere:  IP in a sentence, price in a description

url = "Visit us at https://example.com for more info"

# match fails — string doesn't start with https
print("match :", re.match(r"https://\S+", url))   # None
# search finds it in the middle
print("search:", re.search(r"https://\S+", url))  # <Match 'https://example.com'>

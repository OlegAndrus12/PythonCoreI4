import re

# --- starts with ---
print(bool(re.match(r"^ERROR", "ERROR: disk full")))     # True
print(bool(re.match(r"^ERROR", "WARNING: disk full")))   # False

print()

# --- ends with ---
print(bool(re.search(r"\.py$", "main.py")))              # True
print(bool(re.search(r"\.py$", "main.js")))              # False

print()

# --- both: exact format validation ---
dates = ["2026-04-28", "28-04-2026", "2026-4-8", "not-a-date"]
for d in dates:
    valid = bool(re.match(r"^\d{4}-\d{2}-\d{2}$", d))
    print(f"{d:15} → {valid}")

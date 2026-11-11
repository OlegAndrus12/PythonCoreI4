# lambda — an anonymous one-expression function
# syntax: lambda <args>: <expression>
# Most common use: a short "key" or "callback" passed to another function.

import json
from pathlib import Path

products = [
    {"name": "Laptop", "price": 1200, "rating": 4.5},
    {"name": "Mouse", "price": 25, "rating": 4.8},
    {"name": "Monitor", "price": 300, "rating": 4.5},
    {"name": "Keyboard", "price": 80, "rating": 4.2},
]


# --- BEFORE: a regular named function used once -----------------------------
def get_price(product):
    return product["price"]


cheapest_first = sorted(products, key=get_price)
print([p["name"] for p in cheapest_first])

# --- AFTER: the same function written inline as a lambda --------------------
cheapest_first = sorted(products, key=lambda p: p["price"])
print([p["name"] for p in cheapest_first])


# --- More examples ----------------------------------------------------------

# "best rated first, cheaper wins on a tie" — sort by a tuple of keys
best_deals = sorted(products, key=lambda p: (-p["rating"], p["price"]))
print([p["name"] for p in best_deals])

# max / min with a key
with open(Path(__file__).parent / "employees.json") as json_file:
    employees = json.load(json_file)

top_earner = max(employees, key=lambda e: e["annual_salary"])
youngest = min(employees, key=lambda e: e["age"])
print(f"Top earner: {top_earner['first_name']} {top_earner['last_name']}")
print(f"Youngest: {youngest['first_name']}, {youngest['age']}")

# top-3 most frequent words: sort dict items by value
word_counts = {"python": 12, "java": 7, "rust": 3, "go": 9}
top3 = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:3]
print(top3)

# dispatch table: pick a discount strategy by customer type
discounts = {
    "regular": lambda total: total,
    "member": lambda total: total * 0.9,
    "vip": lambda total: total * 0.8 if total > 100 else total * 0.9,
}
for customer_type, apply_discount in discounts.items():
    print(f"{customer_type:<8} pays {apply_discount(150):.2f} for a 150.00 order")


# --- With employees.json ----------------------------------------------------

# company directory: alphabetical by last name, then first name
directory = sorted(employees, key=lambda e: (e["last_name"], e["first_name"]))
print([f"{e['last_name']}, {e['first_name']}" for e in directory[:5]])

# most experienced first; on a tie, the higher salary goes first
seniority = sorted(employees, key=lambda e: (-e["years_of_experience"], -e["annual_salary"]))
for e in seniority[:3]:
    print(e["first_name"], e["years_of_experience"], e["annual_salary"])

# the salary closest to 100 000
closest = min(employees, key=lambda e: abs(e["annual_salary"] - 100_000))
print(f"Closest to 100k: {closest['first_name']} {closest['annual_salary']}")

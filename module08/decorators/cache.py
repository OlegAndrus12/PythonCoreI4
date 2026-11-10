import json
from functools import wraps
from pathlib import Path

EMPLOYEES_FILE = Path(__file__).parent / "employees.json"


def cache(func):
    store = {}

    @wraps(func)
    def wrapper(*args):
        key = str(args)
        if key not in store:
            store[key] = func(*args)
        else:
            print(f"[cache] hit — returning cached result for args={args}")
        return store[key]

    return wrapper


@cache
def get_employees_by_shirt(shirt_size):
    with open(EMPLOYEES_FILE) as f:
        employees = json.load(f)
    return [
        f"{e['first_name']} {e['last_name']}"
        for e in employees
        if e["shirt_size"] == shirt_size
    ]


@cache
def get_employees_by_ids(ids):
    with open(EMPLOYEES_FILE) as f:
        employees = json.load(f)
    return [
        f"{e['first_name']} {e['last_name']}"
        for e in employees
        if e["id"] in ids
    ]


if __name__ == "__main__":
    print(get_employees_by_shirt("XL"))         # reads file
    print(get_employees_by_shirt("XL"))         # cached
    print(get_employees_by_shirt("M"))          # reads file
    print(get_employees_by_shirt("M"))          # cached

    print(get_employees_by_ids([1, 2, 3]))      # reads file
    print(get_employees_by_ids([1, 2, 3]))      # cached
    print(get_employees_by_ids([4, 5]))         # reads file
    print(get_employees_by_ids([4, 5]))         # cached

# Practice 02 — Password strength checker
#
# Check a password against these rules and report which ones pass/fail:
#   1. At least 8 characters long
#   2. Contains at least one uppercase letter
#   3. Contains at least one lowercase letter
#   4. Contains at least one digit
#   5. Contains at least one special character from: !@#$%^&*
#   6. No spaces allowed
#
# Methods you'll need:
#   len, isupper, islower, isdigit, isspace, count, find

SPECIAL = "!@#$%^&*"

def check_password(password: str) -> dict:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True
        if c in SPECIAL:
            has_special = True
        if c == " ":
            has_space = True

    results = {
        "min_length"  : len(password) >= 8,
        "has_upper"   : has_upper,
        "has_lower"   : has_lower,
        "has_digit"   : has_digit,
        "has_special" : has_special,
        "no_spaces"   : not has_space,
    }
    return results

def strength_label(results: dict) -> str:
    passed = sum(results.values())
    if passed == len(results):
        return "Strong"
    elif passed >= 4:
        return "Medium"
    else:
        return "Weak"

def report(password: str):
    results = check_password(password)
    label = strength_label(results)
    print(f"\nPassword: {password!r}  →  {label}")
    for rule, ok in results.items():
        status = "+" if ok else "-"
        print(f"  {status} {rule.replace('_', ' ')}")

passwords = [
    "hello",
    "Hello123",
    "Hello123!",
    "no spaces here!",
    "N0Sp3c!al",
]

for pw in passwords:
    report(pw)

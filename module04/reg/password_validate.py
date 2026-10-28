import re

def validate_password(pw):
    checks = {
        "min 8 chars":      r".{8,}",
        "uppercase letter": r"[A-Z]",
        "lowercase letter": r"[a-z]",
        "digit":            r"\d",
        "special char":     r"[!@#$%^&*()_+\-=]",
    }
    failed = [
        label
        for label, pat in checks.items()
        if not re.search(pat, pw)
    ]

    if not failed:
        return "Strong password"
    
    return "Weak — missing: " + ", ".join(failed)

passwords = ["secret", "Secret1!", "S3cr3t!X"]
for pw in passwords:
    print(f"{pw:15} → {validate_password(pw)}")

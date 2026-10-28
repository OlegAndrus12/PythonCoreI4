import re

# URL slug generator, regex version of methods/slugify.py
#   "Hello, World!"          → "hello-world"
#   "  10 Tips for Python  " → "10-tips-for-python"
#   "C++ vs Python 3.12???"  → "c-vs-python-3-12"

# [^a-z0-9]  — any character that is NOT a lowercase letter or a digit
# +          — one or more in a row, so ", " or "???" becomes a single "-"
NOT_ALLOWED = r"[^a-z0-9]+"


def slugify(title: str) -> str:
    # 1. lowercase, then replace every run of other characters with one hyphen
    slug = re.sub(NOT_ALLOWED, "-", title.lower())

    # 2. remove hyphens left at the start and the end
    return slug.strip("-")


titles = [
    "Hello, World!",
    "  10 Tips for Python  ",
    "C++ vs Python 3.12???",
    "What is OOP? (Object-Oriented Programming)",
    "FastAPI: Building REST APIs in 2025",
    "Python - the good parts",
    "  ",
]

for title in titles:
    slug = slugify(title)
    print(f"{title:<50} → {slug!r}")


# --- the same idea in one expression, without .strip() ---
# ^-+|-+$  — hyphens at the start (^) OR (|) at the end ($)
def slugify_one_line(title: str) -> str:
    return re.sub(r"^-+|-+$", "", re.sub(NOT_ALLOWED, "-", title.lower()))


print(slugify_one_line("  !!Hello, World!!  "))  # hello-world


# --- alternative: findall the words, then join them ---
# [a-z0-9]+  — one or more letters or digits = one "word" of the slug
def slugify_findall(title: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", title.lower()))


print(slugify_findall("C++ vs Python 3.12???"))  # c-vs-python-3-12

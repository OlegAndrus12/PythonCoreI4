# Practice 04 — URL slug generator
#
# Blog platforms turn article titles into URL-friendly slugs:
#   "Hello, World!"          → "hello-world"
#   "  10 Tips for Python  " → "10-tips-for-python"
#   "C++ vs Python 3.12???"  → "c-vs-python-312"
#
# Methods you'll need:
#   strip, lower, translate, maketrans, split, join

from string import ascii_lowercase, digits

ALLOWED = ascii_lowercase + digits + "- "

def slugify(title: str) -> str:
    # 1. remove surrounding whitespace, lowercase everything
    result = title.strip().lower()

    # 2. drop any character that is not a letter, digit, space, or hyphen
    clean = ""
    for char in result:
        if char in ALLOWED:
            clean += char
        else:
            clean += " "   # replace special chars with space so words still split

    # 3. split on whitespace (handles multiple spaces automatically)
    words = clean.split()

    # 4. join words with a hyphen
    return "-".join(words)


titles = [
    "Hello, World!",
    "  10 Tips for Python  ",
    "C++ vs Python 3.12???",
    "What is OOP? (Object-Oriented Programming)",
    "FastAPI: Building REST APIs in 2025",
    "  ",
]

for title in titles:
    slug = slugify(title)
    print(f"{title:<50} → {slug!r}")

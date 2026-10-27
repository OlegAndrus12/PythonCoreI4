# Checking what a string is made of

# isdigit — all characters are digits (0-9)
print("123".isdigit())       # True
print("12.3".isdigit())      # False  (dot is not a digit)
print("12a".isdigit())       # False

# isalpha — all characters are letters
print("hello".isalpha())     # True
print("hello!".isalpha())    # False
print("привіт".isalpha())    # True  (Unicode letters count)

# isalnum — letters OR digits, no spaces/symbols
print("abc123".isalnum())    # True
print("abc 123".isalnum())   # False  (space breaks it)

# isspace — only whitespace characters
print("   ".isspace())       # True
print("  a  ".isspace())     # False

# isupper / islower
print("HELLO".isupper())     # True
print("Hello".isupper())     # False
print("hello".islower())     # True

# practical: validate user input
def get_age(raw: str) -> int | None:
    cleaned = raw.strip()
    if cleaned.isdigit():
        return int(cleaned)
    return None

print(get_age("  25 "))   # 25
print(get_age("25abc"))   # None

import re

phones = [
    "0671234567",
    "+380671234567",
    "067 123 45 67",
    "(067) 123-45-67",
]

def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)
    digits = re.sub(r"^38", "", digits)
    return f"+38-0{digits[1:3]}-{digits[3:6]}-{digits[6:8]}-{digits[8:10]}"

for p in phones:
    print(f"{p:25} → {normalize_phone(p)}")

import re

# --- 1. Basic: split on any whitespace run (like str.split() but with regex) ---
line = "name:   John   age:  30      city:          Kyiv"
print(re.split(r"\s+", line))
# ['name:   John', 'age:  30', 'city:  Kyiv']

# --- 2. Parse a CSV-like row that uses , or ; or | as delimiter ---
row = "Alice,30;Kyiv|engineer"
print(re.split(r"[,;|]", row))
# ['Alice', '30', 'Kyiv', 'engineer']

# --- 3. Split a sentence into words, stripping punctuation as delimiters ---
sentence = "Wait... are you sure? Yes! I'm sure."
print(re.split(r"[\s.,!?]+", sentence.strip()))
# ['Wait', 'are', 'you', 'sure', 'Yes', "I'm", 'sure']

# --- 4. maxsplit — split only the first N occurrences ---
log = "ERROR:disk:read:failed"
print(re.split(r":", log, maxsplit=1))   # ['ERROR', 'disk:read:failed']
print(re.split(r":", log, maxsplit=2))   # ['ERROR', 'disk', 'read:failed']

# --- 5. Keep the delimiter by wrapping pattern in a capturing group ---
text = "one1two2three3four"
print(re.split(r"(\d)", text))
# ['one', '1', 'two', '2', 'three', '3', 'four']

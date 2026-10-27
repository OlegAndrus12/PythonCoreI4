# Case methods + searching inside strings

text = "the quick brown fox jumps over the lazy dog"

# --- case ---
print(text.upper())           # THE QUICK BROWN FOX ...
print(text.capitalize())      # The quick brown fox ...  (only first letter)
print(text.title())           # The Quick Brown Fox ...  (every word)
print("hElLo".swapcase())     # HeLlO

# --- startswith / endswith ---
url = "https://goit.ua/python"
print(url.startswith("https"))          # True
print(url.endswith(".py"))              # False

# accepts a tuple — any match → True
filename = "report.xlsx"
print(filename.endswith((".xlsx", ".csv", ".json")))   # True

# --- count ---
sentence = "banana"
print(sentence.count("a"))             # 3
print(sentence.count("an"))            # 2

# --- find vs index ---
# find returns -1 when not found; index raises ValueError
s = "hello world"
print(s.find("world"))    # 6
print(s.find("python"))   # -1

try:
    print(s.index("python"))
except ValueError as e:
    print(e)              # substring not found

# rfind — searches from the right
log = "error: disk error: timeout"
print(log.rfind("error"))             # 18  (last occurrence)

# --- zfill — pad with leading zeros (useful for codes/IDs) ---
print("7".zfill(4))        # 0007
print("42".zfill(6))       # 000042

# --- center / ljust / rjust ---
label = "Python"
print(label.center(20, "-"))   # -------Python-------
print(label.ljust(20, "."))    # Python..............
print(label.rjust(20, "."))    # ..............Python

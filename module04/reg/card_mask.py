import re

chat = (
    "Hi, my card is 4111 2222 3333 4444 and I can't complete payment. "
    "I also tried 5500-0000-0000-0004 but same issue."
)

# \b        — word boundary (no digits before/after the card number)
# (\d{4})   — capture group: exactly 4 digits  (repeated 4 times)
# [\s-]     — separator between groups: space or dash
# \4        — backreference to group 4 (last 4 digits kept visible)

CARD = r"\b(\d{4})[\s-](\d{4})[\s-](\d{4})[\s-](\d{4})\b"

masked = re.sub(CARD, r"**** **** **** \4", chat)
print(masked)


# --- getting a specific group ---
# search() returns the first match; group numbers start at 1
# group(0) / group() — the whole match
m = re.search(CARD, chat)
if m:
    print(m.group())      # 4111 2222 3333 4444
    print(m.group(1))     # 4111  — first 4 digits
    print(m.group(4))     # 4444  — last 4 digits
    print(m[4])           # 4444  — same as m.group(4)
    print(m.group(1, 4))  # ('4111', '4444')  — several groups at once
    print(m.groups())     # ('4111', '2222', '3333', '4444')  — all groups

# finditer() — a Match object for every card, so group() works for each
for m in re.finditer(CARD, chat):
    print(f"card ending in {m.group(4)}")

# findall() with several groups — a list of tuples, pick the group by index (0-based!)
for groups in re.findall(CARD, chat):
    print(groups[3])      # last 4 digits

# named groups — access by name instead of number
NAMED = r"\b(?P<first>\d{4})[\s-]\d{4}[\s-]\d{4}[\s-](?P<last>\d{4})\b"
m = re.search(NAMED, chat)
print(m.group("first"), m["last"])  # 4111 4444
print(m.groupdict())                # {'first': '4111', 'last': '4444'}

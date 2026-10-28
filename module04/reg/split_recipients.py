import re

# Practice: the "To:" field of an email form
#
# Users paste recipients in any format: commas, semicolons, spaces, new lines,
# sometimes several separators in a row. str.split() takes only ONE separator,
# re.split() takes a pattern, so all of them are handled at once.

recipients = """olena@example.com, Taras@Example.com;  ivan@example.com
maria@example.com;;  olena@example.com ,
   bad-address, petro@example.com,"""

# [,;\s]  — a comma, a semicolon or any whitespace (space, tab, new line)
# +       — one or more in a row, so ";;  " is ONE separator, not four
SEPARATORS = r"[,;\s]+"

parts = re.split(SEPARATORS, recipients)
print(parts)
# ['olena@example.com', 'Taras@Example.com', 'ivan@example.com', 'maria@example.com',
#  'olena@example.com', 'bad-address', 'petro@example.com', '']

# Why is there an empty string '' at the end?
# The text ENDS with a separator (","), and re.split() returns what is after it: nothing.
# The same happens when the text STARTS with a separator.
# Rule to remember: re.split() can return '' at the edges, so always filter them out.
print(re.split(SEPARATORS, ", a, b,"))  # ['', 'a', 'b', '']

# A simple email check: something@something.something
EMAIL = r"[\w.+-]+@[\w-]+\.[\w.]+"


def parse_recipients(text: str) -> tuple[list[str], list[str]]:
    valid, invalid = [], []
    for part in re.split(SEPARATORS, text.strip()):
        if not part:
            continue  # skip empty strings
        email = part.lower()
        if not re.fullmatch(EMAIL, email):
            invalid.append(part)
        elif email not in valid:  # skip duplicates, keep the original order
            valid.append(email)
    return valid, invalid


valid, invalid = parse_recipients(recipients)
print("Send to:", valid)
# Send to: ['olena@example.com', 'taras@example.com', 'ivan@example.com',
#           'maria@example.com', 'petro@example.com']
print("Check these:", invalid)  # Check these: ['bad-address']


# --- Bonus: split a text into sentences, keeping the punctuation ---
# (?<=[.!?])  — lookbehind: the position right AFTER . ! or ?
# \s+         — the spaces after it are the separator (and are removed)
# The . ! ? themselves are not part of the separator, so they stay in the sentence.
review = "Great course! The regex part was hard. Will there be more practice? Thanks."

for number, sentence in enumerate(re.split(r"(?<=[.!?])\s+", review), start=1):
    print(f"{number}. {sentence}")
# 1. Great course!
# 2. The regex part was hard.
# 3. Will there be more practice?
# 4. Thanks.

# Compare: splitting ON the punctuation loses it
print(re.split(r"[.!?]\s*", review))
# ['Great course', 'The regex part was hard', 'Will there be more practice', 'Thanks', '']

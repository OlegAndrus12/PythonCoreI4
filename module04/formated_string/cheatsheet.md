# Python f-string / Format Cheatsheet

## Format spec syntax
```
{value:[fill][align][sign][#][0][width][grouping]["."precision][type]}
```

---

## Alignment
```python
x = 22
f"{x:<10d}"    # left-aligned,   width 10  → "22        "
f"{x:10d}"     # right-aligned,  width 10  → "        22"
f"{x:^10d}"    # centered,       width 10  → "    22    "
```

Custom fill char goes before align:
```python
f"{x:=<10d}"   # left with '=' fill  → "22========"
f"{x:*^10x}"   # centered with '*'   → "****16****"
f"{x:h>10b}"   # right with 'h' fill → "hhhh10110"
```

---

## Number formatting
```python
n = 1234567.891

f"{n:,.2f}"    # 1,234,567.89   ← comma thousands sep
f"{n:_.2f}"    # 1_234_567.89   ← underscore sep
f"{n:.0f}"     # 1234568        ← no decimal
f"{n:.4f}"     # 1234567.8910   ← 4 decimal places
f"{n:e}"       # 1.234568e+06   ← scientific
f"{n:.2e}"     # 1.23e+06

f"{42:+d}"     # +42            ← always show sign
f"{7:05d}"     # 00007          ← zero-pad to width 5
```

Integer bases:
```python
num = 255
f"{num:b}"     # 11111111  binary
f"{num:o}"     # 377       octal
f"{num:x}"     # ff        hex lower
f"{num:X}"     # FF        hex upper
f"{num:#x}"    # 0xff      with prefix
```

Percentage:
```python
f"{19/22:.2%}"   # 86.36%
f"{0.764:.1%}"   # 76.4%
```

Dynamic width/precision:
```python
width, precision = 12, 3
f"{3.14159:{width}.{precision}f}"   # "       3.142"
```

---

## f-string power features
```python
name = "Oleh"

f"{name!r}"        # 'Oleh'  — repr(), adds quotes
f"{name!s}"        # Oleh    — str() (default)
f"{name!a}"        # 'Oleh'  — ascii(), escapes non-ASCII

x = 42
f"{x=}"            # x=42       — debug shortcut (3.8+)
f"{x=:.2f}"        # x=42.00

# inline expression
score = 73
f"{'pass' if score >= 60 else 'fail'}"   # pass

# multiline — concatenate f-strings in parens
card = (
    f"Name: {name}\n"
    f"Adult: {25 >= 18}"
)
```

---

## Escaping braces
```python
f"{{name}}"            # {name}    ← double braces = literal brace
f"{{{name}}}"          # {Oleh}
f'{{"user": "{name}"}}'  # {"user": "Oleh"}
```

## Python 3.12+ f-strings
```python
f"{person["name"]}"            # same quotes inside — OK in 3.12+
f"{"\n".join(words)}"          # backslash inside — OK in 3.12+
f"{
    total * (1 - discount)  # comment inside
:.2f}"
```

---

## Older styles: `%` and `str.format()`
```python
"%s is %d" % (name, age)            # Oleh is 25
"%.2f" % 49.95                      # 49.95
"%-10s|" % name                     # "Oleh      |"
"%d%%" % 80                         # 80%

"{} is {}".format(name, age)        # by position
"{0} {1} {0}".format("ha", "hi")    # ha hi ha  — by index
"{n}".format(n=name)                # by name
template.format(**data)             # reusable template from a dict
```
`%` style is still the standard in `logging`: `logging.info("User %s", name)`.

---

## String alignment methods
```python
"Python".ljust(10)        # "Python    "
"Python".rjust(10)        # "    Python"
"Python".center(12, "*")  # "***Python***"
"-42".zfill(5)            # "-0042"   ← keeps sign in front
"Python".ljust(3)         # "Python"  ← never truncates
```

---

## Date formatting
`datetime` / `date` take strftime codes after the colon:
```python
from datetime import datetime
d = datetime(2025, 4, 5, 9, 7, 3)

f"{d:%Y-%m-%d}"         # 2025-04-05     ISO
f"{d:%d.%m.%Y}"         # 05.04.2025     European
f"{d:%H:%M:%S}"         # 09:07:03       24-hour
f"{d:%I:%M %p}"         # 09:07 AM       12-hour
f"{d:%A, %d %B %Y}"     # Saturday, 05 April 2025
f"{d:%a %d %b}"         # Sat 05 Apr
f"{d:%d.%m — 100%% done}"  # 05.04 — 100% done   ← %% for literal %

fmt = "%Y/%m/%d"
f"{d:{fmt}}"            # 2025/04/05     format from a variable
```

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` / `%y` | year, 4 / 2 digits | 2025 / 25 |
| `%m` | month 01–12 | 04 |
| `%d` | day 01–31 | 05 |
| `%H` / `%I` | hour 00–23 / 01–12 | 09 |
| `%M` / `%S` | minute / second | 07 / 03 |
| `%p` | AM / PM | AM |
| `%A` / `%a` | weekday full / short | Saturday / Sat |
| `%B` / `%b` | month full / short | April / Apr |
| `%j` | day of year | 095 |
| `%W` | week number (Monday first) | 13 |
| `%w` | weekday, Sunday = 0 | 6 |

Gotcha: the whole spec goes to strftime, so width/align don't work. Format the date first, then align it:
```python
f"{d:%d.%m.%Y:>15}"     # 05.04.2025:>15   ← NOT aligned
s = f"{d:%d.%m.%Y}"
f"{s:>15}"              # "     05.04.2025"
```

`timedelta` has no format codes. Use `str()` or `divmod`:
```python
f"{timedelta(hours=2, minutes=5)}"   # 2:05:00
```

---

## Special escape sequences
```python
"\n"   # newline
"\t"   # horizontal tab
"\r"   # carriage return (moves cursor to line start)
"\f"   # form feed / new page
"\v"   # vertical tab
```

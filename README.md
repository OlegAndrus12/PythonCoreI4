# Python Core

**English** · [Українська](README.uk.md)

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

Lecture materials for the Python Core course. Each module is one lecture: slides, a lecture plan, and
interactive pages and scripts that make **one idea** concrete — run it, change it, read why the output
changed.

Modules are added as lectures happen; the complete previous iteration is [PythonCoreI3](https://github.com/OlegAndrus12/PythonCoreI3).

<img src="yoda.jpg" alt="May the Force be with you" width="280">

```
├── module01/   Data types: built-in types, mutability, typing, operator precedence, collections, conversions
├── module02/   Control flow: if / elif / else, the ternary operator, for and while loops, exceptions, first functions
├── module03/   Dates, times and randomness: datetime, timedelta, time zones, UTC, time, calendar, random
├── module04/   Strings: f-strings and format specs, older formatting styles, string methods, special characters, regex
```

**Conventions used throughout:**

- Each module has an `agenda.md` with the lecture plan (in Ukrainian); slides are added as a PDF where there are any.
- The `.html` pages are self-contained: open them straight from disk in a browser, no server or install needed.
- Every result shown in an HTML page comes from actually running that example on CPython 3.14.3.
- Every script runs on its own: `python module01/strings/basics.py`. Scripts in `module02/if_statements/` and `module02/while_loop/`, and `module04/methods/_strip.py`, ask for input.

---

# Module 01 — Data types

What every built-in type is, what it can do, and the ideas that explain most beginner surprises:
names are references, some objects change in place and others never do, and Python checks types at
runtime but never converts them silently.

| File                                                          | What it is                                                                                                                                                                                                       |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[python-data-types.html](module01/python-data-types.html)** | Interactive cheat sheet: one tab per built-in type, plus five concept tabs (below)                                                                                                                               |
| **[visualizer.html](module01/visualizer.html)**               | Type `a = [1, "hi"]`, `b = a`, `a.append(99)`, `del a` and watch names point at objects on the heap — with reference counts, small-int interning, garbage collection and the bytecode for each line |
| **[collections.md](module01/collections.md)**                 | `list` / `tuple` / `set` / `dict` / `str` compared in one table, the time complexity of each operation, and when to use which                                                                                   |
| **[strong_dynamic.txt](module01/strong_dynamic.txt)**         | Static vs dynamic typing: advantages and disadvantages of each                                                                                                                                                   |
| **[Intro.pdf](module01/Intro.pdf)**                           | Lecture slides                                                                                                                                                                                                   |

**Example scripts** — each one a real-world scenario (a playlist, a user profile, an API response):

| Script                                                                                                    | What it shows                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [strings/basics.py](module01/strings/basics.py)                                                           | Three ways to format a string, case methods, search and check, modify, split and join, slicing, `IndexError`                                    |
| [lists/basics.py](module01/lists/basics.py)                                                               | A playlist: adding, removing and finding tracks, sorting (incl. `key=len`), slicing, copying, `IndexError`                                       |
| [tuples/basics.py](module01/tuples/basics.py)                                                             | Creating (and the single-element trailing comma), accessing, unpacking, immutability, methods, tuple vs list, tuples as dict keys               |
| [tuples/use_cases.py](module01/tuples/use_cases.py)                                                       | Eight real uses: coordinates, returning several values, unpacking CSV rows, composite keys, deduplicating records, swap, constants, sort keys    |
| [sets/basics.py](module01/sets/basics.py)                                                                 | `add` / `remove` / `discard`, deduplication, set operations — with a [diagram](module01/sets/Python-Set-Operatioons.png)                          |
| [dicts/basics.py](module01/dicts/basics.py)                                                               | A user profile, a store product, an HTTP response, app settings; what can and can't be a key; `KeyError`                                        |
| [dicts/list_of_dicts.py](module01/dicts/list_of_dicts.py)                                                 | A list of dicts — starting data for exercises                                                                                                    |
| [conversions/basics.py](module01/conversions/basics.py)                                                   | Converting between `int`, `float`, `bool`, `None`, `str`, `list`, `set` and `dict`, and chained conversions                                     |
| [deposit.py](module01/deposit.py)                                                                         | Parse `KEY=value` config lines into a dict, skipping comments                                                                                   |

**The cheat sheet, tab by tab:**

| Tab                                                   | What's in it                                                                                                                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `int` `None` `str` `bool` `list` `dict` `tuple` `set` | Literals, key properties, every public method with an example, and the operations that trip people up. `bool` adds a truth table                             |
| **Змінність** — mutability                            | A map of mutable vs immutable types; memory diagrams of `b.append()` vs `t += '!'`; consequences for dict keys, default arguments and copying                |
| **Типізація** — typing                                | Static/dynamic × strong/weak on one chart; when a type error is caught (compile time, runtime, or mypy); the same expression in Python, JavaScript and Java  |
| **Пріоритети** — operator precedence                  | All 18 levels with associativity, an expression tree showing how Python brackets `1 + 2 * 3 ** 2 > 10 and not False`, and 17 traps like `-2 ** 2`            |
| **Колекції** — collections                            | `list` / `tuple` / `set` / `dict` / `str` side by side, the Big-O of each operation, why `in` is O(1) for a set, and a "which one do I need?" flowchart      |
| **Порівняння** — comparison                           | All eight types in one table                                                                                                                                 |

📋 Full topic list: **[module01/agenda.md](module01/agenda.md)**

---

# Module 02 — Control flow

Making a program choose and repeat: branching with `if`, looping with `for` and `while`, the built-ins
that make loops readable, and handling exceptions. The lecture ends with the idea of functions.

| File                                                                      | What it is                                                                                                                         |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **[python-control-flow.html](module02/python-control-flow.html)**         | Interactive cheat sheet: one tab each for `if`, `while`, `for` and `try` / `except` — syntax, key rules, a step-by-step view of how the interpreter runs it, the exception hierarchy, examples and pitfalls |
| **[caesar_visualizer.html](module02/functions/caesar/caesar_visualizer.html)** | Caesar cipher, letter by letter: each letter becomes a number, gets shifted, and wraps around; with the full substitution table |

**`if` statements** — interactive, each script asks for input:

| Script                                                     | What it shows                                                                 |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [if_statements/01.py](module02/if_statements/01.py)        | A login check: nested `if` / `elif` / `else`                                  |
| [if_statements/02.py](module02/if_statements/02.py)        | Comparing two numbers                                                         |
| [if_statements/03.py](module02/if_statements/03.py)        | Combining conditions with `and` / `or`                                        |
| [if_statements/04.py](module02/if_statements/04.py)        | Membership checks with `in` / `not in`                                        |
| [if_statements/06.py](module02/if_statements/06.py)        | Leap year — the order of the conditions matters                               |
| [if_statements/ternary.py](module02/if_statements/ternary.py) | The ternary operator: `value_if_true if condition else value_if_false`     |

**`for` loops:**

| Script                                                                            | What it shows                                                          |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [for_loop/basics.py](module02/for_loop/basics.py)                                 | Looping over a list, a string, and `range`                             |
| [for_loop/break_continue.py](module02/for_loop/break_continue.py)                 | `break` at the first critical log line; `continue` to skip items       |
| [for_loop/building_collections.py](module02/for_loop/building_collections.py)     | Filtering into a new list: `.py` files, failed HTTP responses          |
| [for_loop/enumerate.py](module02/for_loop/enumerate.py)                           | `enumerate(..., start=1)` — a numbered commit log                      |
| [for_loop/zip.py](module02/for_loop/zip.py)                                       | `zip` — walking two lists in step                                      |
| [for_loop/nested.py](module02/for_loop/nested.py)                                 | Nested loops: a weekly schedule, round-robin matchups                  |

**`while` loops** — interactive, each script asks for input:

| Script                                                          | What it shows                                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [while_loop/digit_sum.py](module02/while_loop/digit_sum.py)     | Sum of the digits of a number with `% 10` and `//= 10`                                |
| [while_loop/guess.py](module02/while_loop/guess.py)             | Guess the number: loop until the answer is right, counting attempts                  |
| [while_loop/menu.py](module02/while_loop/menu.py)               | A game menu: `while True` with `break` to quit and `continue` on bad input            |
| [while_loop/menu_enum.py](module02/while_loop/menu_enum.py)     | The same menu with an `Enum` and `match` / `case` instead of string comparisons      |

**Functions:**

| Script                                                          | What it shows                                                                                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [functions/01_functions.py](module02/functions/01_functions.py) | A clinic check-in: BMI, default and named arguments, validating input and returning early, returning several values, combining small functions |
| [functions/caesar/main.py](module02/functions/caesar/main.py)   | `encrypt(key, message)` — the Caesar cipher behind the visualizer                                                                    |

📋 Full topic list: **[module02/agenda.md](module02/agenda.md)**

---

# Module 03 — Dates, times and random numbers

Working with dates and times — creating, formatting, parsing, doing arithmetic, and converting between
time zones — plus the `random` module.

| File                                                              | What it is                                                                                                                                                        |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[python-date-random.html](module03/python-date-random.html)**   | Interactive cheat sheet: tabs for `datetime`, `date`, `time`, `timedelta`, time zones (`timezone` and `zoneinfo`), UTC, the `time` module, `calendar`, `random`, all `strftime` / `strptime` codes, and ready-made recipes |
| **[formats.md](module03/formats.md)**                             | Every `strftime` / `strptime` format code, each shown on the same reference date                                                                                 |

**Date and time scripts:**

| Script                                                                                    | What it shows                                                                                                    |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [date/01_dt.py](module03/date/01_dt.py)                                                   | Creating a `datetime`, splitting it into `date()` and `time()`, `now()` and `today()`                            |
| [date/02_dt.py](module03/date/02_dt.py)                                                   | Parsing a string with `strptime`, `replace()`, subtracting two datetimes gives a `timedelta`                    |
| [date/03_dt.py](module03/date/03_dt.py)                                                   | Adding a `timedelta` to the current time                                                                         |
| [date/04_dt.py](module03/date/04_dt.py)                                                   | `strftime("%B")` / `"%A"` — the month or weekday name of a date                                                  |
| [date/05_dt.py](module03/date/05_dt.py)                                                   | Every day between two dates with `range` and `timedelta(days=i)`                                                 |
| [date/06_dt.py](module03/date/06_dt.py)                                                   | Ordinal, timestamp, `ctime` and ISO format — and restoring a datetime from each                                  |
| [date/07_dt.py](module03/date/07_dt.py)                                                   | `datetime.combine`, `timedelta.total_seconds()`, going back in time                                              |
| [date/08_dt.py](module03/date/08_dt.py)                                                   | `calendar`: `isleap`, `monthrange`, `weekday`, `monthcalendar`                                                   |
| [date/09_age_and_birthdays.py](module03/date/09_age_and_birthdays.py)                     | HR / CRM: exact age, and who on the team has a birthday this week (including 29 February)                       |
| [date/10_utc.py](module03/date/10_utc.py)                                                 | UTC step by step: naive vs aware, converting to and from local time, fixed offsets vs `ZoneInfo` and DST         |
| [date/11_log_parsing.py](module03/date/11_log_parsing.py)                                 | DevOps: parse timestamps from a log and print them in ISO and human-readable form                               |
| [date/12_meeting_across_timezones.py](module03/date/12_meeting_across_timezones.py)       | One meeting shown in Kyiv, Stockholm and Texas time; why naive and aware can't be mixed                          |
| [date/timezones3.py](module03/date/timezones3.py)                                         | `zoneinfo` (standard library): attaching a zone, converting with `astimezone()`, making a naive datetime aware   |
| [date/timezones.py](module03/date/timezones.py), [timezones2.py](module03/date/timezones2.py) | The same with the third-party `pytz` and `dateutil` packages (`pip install pytz python-dateutil`)            |
| [date/calend.py](module03/date/calend.py)                                                 | `calendar.calendar(year)` and `calendar.month_name`                                                              |
| [date/deal_time.py](module03/date/deal_time.py)                                           | `time.sleep()` in a loop                                                                                         |

**`random` scripts:**

| Script                                              | What it shows                                                                          |
| --------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [random/01_rd.py](module03/random/01_rd.py)         | `randint` — a coin flip                                                                |
| [random/02_rd.py](module03/random/02_rd.py)         | Flip a coin until one side comes up four times in a row                               |
| [random/03_rd.py](module03/random/03_rd.py)         | Bogosort: `shuffle` a list until it happens to be sorted                              |
| [random/04_rd.py](module03/random/04_rd.py)         | `choices` — generate a random licence plate                                            |
| [random/05_rd.py](module03/random/05_rd.py)         | `choice` vs `sample` vs `choices`: one item, unique items, items that can repeat       |
| [random/06_rd.py](module03/random/06_rd.py)         | `random()`, `uniform()`, and `seed()` for reproducible results                         |

📋 Full topic list: **[module03/agenda.md](module03/agenda.md)**

---

# Module 04 — Strings and regular expressions

Formatting output exactly the way you want it, the string methods you'll use every day, and (coming in
part 2) regular expressions for finding text by its shape.

| File                                                                    | What it is                                                                                                                                                       |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[python-strings-regex.html](module04/python-strings-regex.html)**     | Interactive cheat sheet: tabs for f-strings, `%` and `str.format()`, `str` methods, the `re` module, the full format spec, escape sequences and raw strings, and regex syntax |
| **[formated_string/cheatsheet.md](module04/formated_string/cheatsheet.md)** | The format spec in one page: alignment and fill, numbers, bases, percentages, dates                                                                          |

**String formatting:**

| Script                                                                            | What it shows                                                                                              |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [formated_string/01.py](module04/formated_string/01.py)                           | Left, right and center alignment in a fixed width                                                          |
| [formated_string/02.py](module04/formated_string/02.py)                           | A table of the numbers 0–15 in decimal, hex and binary                                                     |
| [formated_string/03.py](module04/formated_string/03.py)                           | `:.2%` vs building a percentage by hand                                                                    |
| [formated_string/04.py](module04/formated_string/04.py)                           | `f"{x=}"` for debugging, multiline f-strings, a conditional inside `{}`                                    |
| [formated_string/05.py](module04/formated_string/05.py)                           | Numbers: thousands separators, precision, scientific notation, sign, zero-padding, bases, percentages      |
| [formated_string/06.py](module04/formated_string/06.py)                           | Dates in f-strings: `f"{d:%d.%m.%Y}"`, why alignment doesn't work there, formatting a `timedelta`          |
| [formated_string/08.py](module04/formated_string/08.py)                           | The older styles: the `%` operator and `str.format()`, and reusable templates                              |
| [formated_string/09.py](module04/formated_string/09.py)                           | `ljust`, `rjust`, `center`, `zfill` — and a table of contents with dot leaders                             |
| [formated_string/10.py](module04/formated_string/10.py)                           | Practice: a shop receipt with aligned columns, a discount and a total                                      |
| [formated_string/special_symbols.py](module04/formated_string/special_symbols.py) | `\n`, `\f`, `\r`, `\t`, `\v` — what each one does to the output                                            |

**String methods:**

| Script                                                                      | What it shows                                                                                    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [methods/_case_and_search.py](module04/methods/_case_and_search.py)         | Case methods, `startswith` / `endswith`, `count`, `find` vs `index`, `rfind`, padding           |
| [methods/_isdigit_isalpha.py](module04/methods/_isdigit_isalpha.py)         | `isdigit`, `isalpha`, `isalnum`, `isspace`, `isupper` / `islower`; validating user input         |
| [methods/_split.py](module04/methods/_split.py)                             | `split`: the longest word, the longest chain of vowels                                           |
| [methods/_join.py](module04/methods/_join.py)                               | `join` — a sorted list of dict keys as one line                                                  |
| [methods/_replace.py](module04/methods/_replace.py)                         | `replace` in a loop to collapse repeated commas                                                  |
| [methods/_strip.py](module04/methods/_strip.py)                             | `strip` before comparing user input — asks for input                                             |
| [methods/validate_password.py](module04/methods/validate_password.py)       | Practice: a password strength checker that reports which rules pass and which fail               |

📋 Full topic list: **[module04/agenda.md](module04/agenda.md)**

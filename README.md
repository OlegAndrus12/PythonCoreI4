# Python Core

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

Lecture materials for the Python Core course. Each module is one lecture: slides, a lecture plan, and
interactive pages and scripts that make **one idea** concrete — run it, change it, read why the output
changed.

Modules are added as lectures happen; the complete previous iteration is [PythonCoreI3](https://github.com/OlegAndrus12/PythonCoreI3).

<img src="yoda.jpg" alt="May the Force be with you" width="280">

```
├── module01/   Data types: built-in types, mutability, typing, operator precedence, collections, conversions
├── module02/   Control flow: if / elif / else, the ternary operator, for loops
```

**Conventions used throughout:**

- Each module has an `agenda.md` with the lecture plan (in Ukrainian); slides are added as a PDF where there are any.
- The `.html` pages are self-contained: open them straight from disk in a browser, no server or install needed.
- Every result shown in an HTML page comes from actually running that example on CPython 3.14.3.
- Every script runs on its own: `python module01/strings/basics.py`. Scripts in `module02/if_statements/` ask for input.
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

Making a program choose and repeat: branching with `if`, looping over collections with `for`, and the
built-ins that make loops readable. The lecture also covers `while`, the debugger and exceptions.

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

📋 Full topic list: **[module02/agenda.md](module02/agenda.md)**

# Python Core — iteration 4

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

Lecture materials for the Python Core course. Each module is one lecture: slides, a lecture plan, and
interactive pages and scripts that make **one idea** concrete — run it, change it, read why the output
changed.

Modules are added as lectures happen; the complete previous iteration is [PythonCoreI3](https://github.com/OlegAndrus12/PythonCoreI3).

<img src="yoda.jpg" alt="May the Force be with you" width="280">

```
├── module01/   Data types: built-in types, mutability, typing, operator precedence, collections
```

**Conventions used throughout:**

- Each module has an `agenda.md` with the lecture plan and the slides as a PDF (both in Ukrainian).
- The `.html` pages are self-contained: open them straight from disk in a browser, no server or install needed.
- Every result shown in an HTML page comes from actually running that example on CPython 3.14.3.
- Every script runs on its own: `python module01/deposit.py`.

---

# Module 01 — Data types

What every built-in type is, what it can do, and the ideas that explain most beginner surprises:
names are references, some objects change in place and others never do, and Python checks types at
runtime but never converts them silently.

| File                                                               | What it is                                                                                                                                                                                                  |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[python-data-types.html](module01/python-data-types.html)** | Interactive cheat sheet: one tab per built-in type, plus four concept tabs (below)                                                                                                                          |
| **[visualizer.html](module01/visualizer.html)**               | Type`a = [1, "hi"]`, `b = a`, `a.append(99)`, `del a` and watch names point at objects on the heap — with reference counts, small-int interning, garbage collection and the bytecode for each line |
| **[deposit.py](module01/deposit.py)**                         | Compound interest — numbers and operators in one small real calculation                                                                                                                                    |
| **[Design.pdf](module01/Design.pdf)**                         | Lecture slides                                                                                                                                                                                              |

**The cheat sheet, tab by tab:**

| Tab                                                                   | What's in it                                                                                                                                                        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `int` `None` `str` `bool` `list` `dict` `tuple` `set` | Literals, key properties, every public method with an example, and the operations that trip people up.`bool` adds a truth table                                   |
| **Змінність** — mutability                            | A map of mutable vs immutable types; memory diagrams of`b.append()` vs `t += '!'`; consequences for dict keys, default arguments and copying                    |
| **Типізація** — typing                                | Static/dynamic × strong/weak on one chart; when a type error is caught (compile time, runtime, or mypy); the same expression in Python, JavaScript and Java        |
| **Пріоритети** — operator precedence                 | All 18 levels with associativity, an expression tree showing how Python brackets`1 + 2 * 3 ** 2 > 10 and not False`, and 17 traps like `-2 ** 2`                |
| **Колекції** — collections                             | `list` / `tuple` / `set` / `dict` / `str` side by side, the Big-O of each operation, why `in` is O(1) for a set, and a "which one do I need?" flowchart |
| **Порівняння** — comparison                          | All eight types in one table                                                                                                                                        |

📋 Full topic list: **[module01/agenda.md](module01/agenda.md)**

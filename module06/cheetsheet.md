# Module 06 — Modules, Packages, pip, and Publishing

---

## 1. How imports work

When you write `import something`, Python searches in this order:

1. **sys.modules** — already-loaded modules cache
2. **Built-in modules** — compiled into the interpreter (`sys`, `os`, `math` …)
3. **sys.path** — list of directories (current dir, venv site-packages, stdlib paths)

```python
import sys
print(sys.path)   # see where Python looks
```

---

## 2. Module / Package / Script / File

| Term | What it is |
|------|-----------|
| **file** | any `.py` file |
| **module** | a `.py` file you `import` |
| **package** | a directory with `__init__.py` |
| **script** | a `.py` file you run directly (`python foo.py`) |

A file can be both a module and a script at the same time.

---

## 3. `__name__` and entry points

Every Python file has a `__name__` variable.

- When **imported**: `__name__` is the module name (e.g. `"moskali.main"`)
- When **run directly**: `__name__` is `"__main__"`

```python
def main():
    print("Hello!")

if __name__ == "__main__":
    main()
```

This pattern lets you protect "startup" code so it only runs when the file is executed directly, not when imported.

---

## 4. `__init__.py`

Makes a directory a **package**. Runs automatically on import.

```
moskali/
    __init__.py      ← runs on `import moskali`
    main.py
    utils.py
```

Use it to control what `from moskali import *` exposes, or to re-export things:

```python
# __init__.py
from moskali.main import main   # now `from moskali import main` works
```

An empty `__init__.py` is totally fine — it just marks the folder as a package.

---

## 5. pip and PyPI

**pip** — *Pip Installs Packages* (or *Preferred Installer Program*)  
**PyPI** — *Python Package Index* at [pypi.org](https://pypi.org) — the public registry

```bash
pip install requests          # install latest
pip install requests==2.31.0  # install specific version
pip install -r requirements.txt  # install from a file
pip uninstall requests
pip show requests             # info about an installed package
pip list                      # all installed packages
pip freeze                    # installed packages in requirements format
pip freeze > requirements.txt # save your dependencies
pip install --upgrade pip     # update pip itself
```

---

## 6. Virtual environments

Keeps each project's dependencies isolated.

```bash
python -m venv .env           # create venv in .env/
source .env/bin/activate      # activate (Mac/Linux)
.env\Scripts\activate         # activate (Windows)
deactivate                    # exit venv
```

Inside `.env/`:
```
.env/
  bin/          ← python, pip, activated scripts
  lib/          ← site-packages (your installed packages live here)
  pyvenv.cfg    ← points to the base Python
```

---

## 7. Project structure

**DRY** — Don't Repeat Yourself. If you copy-paste code, it belongs in a function or module.  
**KISS** — Keep It Simple, Stupid. Solve the problem in front of you, not the hypothetical one.

Typical layout for a small package:

```
my_package/
    my_package/
        __init__.py
        main.py
        utils.py
    tests/
    README.md
    LICENSE
    pyproject.toml   ← modern build config (replaces setup.py)
    setup.cfg        ← package metadata (used with setuptools)
```

---

## 8. Creating a package with setuptools

### `pyproject.toml` — tells pip which build backend to use

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

### `setup.cfg` — package metadata (modern approach)

```ini
[metadata]
name = moskali
version = 6
description = Very useful code
long_description = file: README.md
long_description_content_type = text/markdown
author = Oleh Andrus
author_email = andrus@test.gmail.com
license = MIT

[options]
packages = find_namespace:
install_requires =
    faker

[options.entry_points]
console_scripts =
    run_main = moskali:main
```

`entry_points` → `console_scripts` creates a terminal command (`run_main`) that calls `main()` from the `moskali` package.

### `setup.py` — older style (still works, still common)

```python
from setuptools import setup, find_namespace_packages

setup(
    name="moskali",
    version="6",
    packages=find_namespace_packages(),
    install_requires=["faker"],
    entry_points={"console_scripts": ["run_main = moskali:main"]},
)
```

### Install locally (editable mode)

```bash
pip install -e .
```

`-e` = *editable* — your code changes take effect immediately without reinstalling. Great during development.

Run it from the folder that has `pyproject.toml` / `setup.cfg` (`module06/moskali`), not from the inner `moskali/moskali` code folder — otherwise pip says *"does not appear to be a Python project"*.

### Check that it works (moskali)

```bash
pip show moskali                  # installed? which version, where from
which moskali                     # the console_scripts command exists (Windows: where moskali)
moskali --help                    # list of all commands

moskali categories                # all categories (English / Ukrainian)
moskali summary                   # cumulative losses with a bar chart
moskali daily --days 3            # daily losses table for the last 3 days
moskali trend drone --days 5      # one category over time (part of a name is enough)
moskali monthly --months 2        # totals per calendar month
moskali period --days 7           # totals for the last 7 days
moskali plot tanks --days 14      # terminal bar chart (uses plotext)
moskali trend xyz                 # unknown category → friendly error, no traceback
```

If you get `command not found: moskali`, the venv where you installed it is not active. Run `source .env/bin/activate` and try again.

---

## 9. Publishing to PyPI with twine

### Step 1 — Build distribution files

```bash
python -m build
```

Creates two files inside `dist/`:
- `.tar.gz` — source distribution
- `.whl` — wheel (binary distribution, faster to install)

### Step 2 — Upload to TestPyPI first (safe!)

```bash
pip install twine
python -m twine upload --repository testpypi dist/*
```

TestPyPI is a sandbox — safe to experiment without polluting the real index.  
Create a free account at [test.pypi.org](https://test.pypi.org).

### Step 3 — Upload to real PyPI

```bash
python -m twine upload dist/*
```

Twine will ask for your PyPI username and password (or API token — use a token, it's safer).

### Step 4 — Install your published package

```bash
pip install --index-url https://test.pypi.org/simple/ moskali  # from TestPyPI
pip install moskali                                              # from real PyPI
```

---

## 10. Useful packages worth knowing

| Package | What it does |
|---------|-------------|
| `requests` | HTTP — the friendliest way to call APIs |
| `httpx` | async-capable modern HTTP client |
| `rich` | beautiful terminal output, tables, progress bars |
| `click` | build CLI tools with decorators |
| `pydantic` | data validation using Python type hints |
| `faker` | generate fake names, emails, dates for testing |
| `python-dotenv` | load `.env` files into environment variables |
| `loguru` | dead-simple logging |
| `tqdm` | progress bars for loops |
| `pytest` | testing framework |

## 11. Silly / fun packages

```bash
pip install cowsay        # a cow says things in the terminal
pip install art           # ASCII art text and random art
pip install pyfiglet      # big ASCII banner text
pip install asciimatics   # terminal animations and effects
pip install emoji         # 🐍 print("I love " + emoji.emojize(":snake:"))
pip install anticache     # does nothing, just has a funny name
pip install antigravity   # `import antigravity` → opens xkcd 353 in browser
pip install this          # `import this` → prints the Zen of Python
```

```python
import cowsay
cowsay.cow("Python is awesome")

import art
art.tprint("GoIT", font="block")

import pyfiglet
print(pyfiglet.figlet_format("Hello!"))
```

---


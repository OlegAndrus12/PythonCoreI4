# moskali

A console tool to visualize Russian military losses data sourced from the Ukrainian General Staff.

## Dependencies

- [rich](https://github.com/Textualize/rich) ≥ 13.0 — terminal tables and styling

## Development setup

```bash
# Install the package in editable mode (changes take effect immediately)
pip install -e .
```

## Usage

```
moskali <command> [options]
```

### Commands

| Command | Description |
|---|---|
| `moskali summary` | Cumulative losses with bar chart |
| `moskali daily [--days N]` | Daily losses table, one column per day |
| `moskali trend [CATEGORY] [--days N]` | Bar chart trend for a single category |
| `moskali period [--days N]` | Net losses over a period |
| `moskali categories` | List all available category names |

### Examples

```bash
moskali summary
moskali daily --days 10
moskali trend UAVs/Drones --days 30
moskali period --days 7
moskali categories
```

## Project structure

```
moskali/
├── pyproject.toml
├── setup.cfg
├── README.md
└── moskali/
    ├── __init__.py
    ├── loader.py     — loads and parses moskali.json
    ├── stats.py      — daily diffs, trends, period totals
    ├── render.py     — rich tables and bar charts
    ├── cli.py        — argparse entry point
    └── moskali.json  — data source
```

## Building and publishing

Install the build tools once:

```bash
pip install build twine
```

Build a source distribution and wheel into `dist/`:

```bash
python -m build
```

Test the upload against Test PyPI first:

```bash
twine upload --repository testpypi dist/*
```

Publish to PyPI:

```bash
twine upload dist/*
```

Credentials can be stored in `~/.pypirc` or passed via `TWINE_USERNAME` / `TWINE_PASSWORD` environment variables.

import plotext as plt
from rich.console import Console
from rich.table import Table
from rich import box

from .loader import CATEGORIES, LABELS

console = Console(soft_wrap=True)

_BAR_CHAR = "█"
_EMPTY_CHAR = "░"


def _bar(value, max_value, width=28):
    if max_value == 0:
        return _EMPTY_CHAR * width
    filled = round(value / max_value * width)
    return f"[red]{_BAR_CHAR * filled}[/red][dim]{_EMPTY_CHAR * (width - filled)}[/dim]"


def print_summary(record):
    date_str = record["date"].strftime("%Y-%m-%d")
    table = Table(
        title=f"Russian Military Losses — Cumulative as of {date_str}",
        box=box.SIMPLE_HEAD,
        show_footer=False,
    )
    table.add_column("Category", style="white", min_width=20)
    table.add_column("Chart", no_wrap=True)
    table.add_column("Total", justify="right", style="bold yellow")

    max_val = max(record[cat] for cat in CATEGORIES if cat != "Особовий склад")
    for cat in CATEGORIES:
        label = LABELS[cat]
        val = record[cat]
        use_max = max_val if cat != "Особовий склад" else val
        table.add_row(label, _bar(val, use_max), f"{val:,}")

    console.print(table)


def print_daily(daily_records):
    dates = [r["date"].strftime("%m/%d") for r in daily_records]
    table = Table(title="Daily Losses", box=box.SIMPLE_HEAD)
    table.add_column("Category", style="white", min_width=20)
    for d in dates:
        table.add_column(d, justify="right")

    for cat in CATEGORIES:
        label = LABELS[cat]
        vals = [r[cat] for r in daily_records]
        cells = [
            f"[yellow]{v:,}[/yellow]" if v > 0 else f"[dim]{v:,}[/dim]"
            for v in vals
        ]
        table.add_row(label, *cells)

    console.print(table)


def print_trend(trend_data, category=""):
    label = LABELS.get(category, category)
    table = Table(
        title=f"Trend: {label}  ({len(trend_data)} days)",
        box=box.SIMPLE_HEAD,
        show_header=False,
    )
    table.add_column("Date", style="cyan", width=6)
    table.add_column("Bar", no_wrap=True)
    table.add_column("Daily", justify="right", style="bold yellow")

    max_daily = max((d for _, _, d in trend_data), default=1) or 1
    for date, _cumulative, daily in trend_data:
        table.add_row(
            date.strftime("%m/%d"),
            _bar(daily, max_daily, 30),
            f"+{daily:,}",
        )

    console.print(table)


def print_categories():
    table = Table(title="Available Categories", box=box.SIMPLE_HEAD)
    table.add_column("#", justify="right", style="dim", width=3)
    table.add_column("English", style="white")
    table.add_column("Ukrainian", style="dim")

    for i, cat in enumerate(CATEGORIES, 1):
        table.add_row(str(i), LABELS[cat], cat)

    console.print(table)


def print_monthly(monthly_records):
    table = Table(title="Monthly Losses", box=box.SIMPLE_HEAD)
    table.add_column("Category", style="white", min_width=20)
    for r in monthly_records:
        table.add_column(r["month"], justify="right")

    for cat in CATEGORIES:
        label = LABELS[cat]
        cells = [f"[yellow]{r[cat]:,}[/yellow]" if r[cat] > 0 else f"[dim]{r[cat]:,}[/dim]"
                 for r in monthly_records]
        table.add_row(label, *cells)

    console.print(table)


def print_plot(records, category, days):
    label = LABELS.get(category, category)
    subset = records[:days + 1]
    daily = [subset[i][category] - subset[i + 1][category] for i in range(len(subset) - 1)]
    dates = [r["date"].strftime("%m/%d") for r in subset[:-1]]

    daily.reverse()
    dates.reverse()

    plt.clear_figure()
    plt.bar(dates, daily, color="red")
    plt.title(f"Daily losses: {label}")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.plotsize(plt.terminal_width(), 30)
    plt.show()


def print_period_totals(totals):
    from_str = totals["from"].strftime("%Y-%m-%d")
    to_str = totals["to"].strftime("%Y-%m-%d")
    table = Table(
        title=f"Losses  {from_str} → {to_str}",
        box=box.SIMPLE_HEAD,
        show_footer=False,
    )
    table.add_column("Category", style="white", min_width=20)
    table.add_column("Chart", no_wrap=True)
    table.add_column("Total", justify="right", style="bold yellow")

    max_val = max(totals[cat] for cat in CATEGORIES if cat != "Особовий склад")
    for cat in CATEGORIES:
        label = LABELS[cat]
        val = totals[cat]
        use_max = max_val if cat != "Особовий склад" else val
        table.add_row(label, _bar(val, use_max), f"+{val:,}")

    console.print(table)

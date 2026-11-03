import argparse
from . import loader, stats, render


def cmd_summary(args):
    data = loader.load()
    render.print_summary(data[0])


def cmd_daily(args):
    data = loader.load()
    daily = stats.daily_losses(data, args.days)
    render.print_daily(daily)


def cmd_trend(args):
    data = loader.load()
    category = args.category
    if category not in loader.CATEGORIES:
        # try matching by English label
        matches = [c for c, l in loader.LABELS.items() if args.category.lower() in l.lower()]
        if matches:
            category = matches[0]
        else:
            print(f"Unknown category '{args.category}'. Run `moskali categories` for a list.")
            return
    trend_data = stats.trend(data, category, args.days)
    render.print_trend(trend_data, category)


def cmd_period(args):
    data = loader.load()
    totals = stats.totals_for_period(data, args.days)
    render.print_period_totals(totals)


def cmd_categories(_args):
    render.print_categories()


def cmd_monthly(args):
    data = loader.load()
    monthly = stats.monthly_losses(data)
    render.print_monthly(monthly[-args.months:])


def cmd_plot(args):
    data = loader.load()
    category = args.category
    if category not in loader.CATEGORIES:
        matches = [c for c, l in loader.LABELS.items() if args.category.lower() in l.lower()]
        if matches:
            category = matches[0]
        else:
            print(f"Unknown category '{args.category}'. Run `moskali categories` for a list.")
            return
    render.print_plot(data, category, args.days)


def main():
    parser = argparse.ArgumentParser(
        prog="moskali",
        description="Visualize Russian military losses data",
    )
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")

    sub.add_parser("summary", help="Latest cumulative snapshot with bar chart")
    sub.add_parser("categories", help="List all available categories")

    p = sub.add_parser("daily", help="Daily losses table")
    p.add_argument("--days", type=int, default=7, metavar="N", help="Number of days (default: 7)")

    p = sub.add_parser("trend", help="ASCII bar chart for one category over time")
    p.add_argument("category", nargs="?", default="Personnel", metavar="CATEGORY",
                   help="Category name in English (default: Personnel)")
    p.add_argument("--days", type=int, default=14, metavar="N", help="Number of days (default: 14)")

    p = sub.add_parser("monthly", help="Total losses per calendar month")
    p.add_argument("--months", type=int, default=6, metavar="N", help="Number of months (default: 6)")

    p = sub.add_parser("period", help="Total losses over a period")
    p.add_argument("--days", type=int, default=30, metavar="N", help="Period in days (default: 30)")

    p = sub.add_parser("plot", help="Terminal bar chart for one category over time")
    p.add_argument("category", nargs="?", default="Personnel", metavar="CATEGORY",
                   help="Category name in English (default: Personnel)")
    p.add_argument("--days", type=int, default=30, metavar="N", help="Number of days (default: 30)")

    args = parser.parse_args()

    dispatch = {
        "summary": cmd_summary,
        "categories": cmd_categories,
        "daily": cmd_daily,
        "trend": cmd_trend,
        "monthly": cmd_monthly,
        "period": cmd_period,
        "plot": cmd_plot,
    }

    if args.command in dispatch:
        dispatch[args.command](args)
    else:
        parser.print_help()

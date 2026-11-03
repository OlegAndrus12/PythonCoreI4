from .loader import CATEGORIES


def daily_losses(records, days=7):
    pairs = list(zip(records[:days], records[1 : days + 1]))
    result = []
    for newer, older in pairs:
        diff = {"date": newer["date"]}
        for cat in CATEGORIES:
            diff[cat] = newer[cat] - older[cat]
        result.append(diff)
    return result


def trend(records, category, days=14):
    subset = records[: days + 1]
    result = []
    for i, rec in enumerate(subset[:-1]):
        daily = rec[category] - subset[i + 1][category]
        result.append((rec["date"], rec[category], daily))
    return result


def monthly_losses(records):
    by_month = {}
    for r in records:
        key = (r["date"].year, r["date"].month)
        if key not in by_month:
            by_month[key] = r  # newest record per month (records are newest-first)

    months = sorted(by_month.values(), key=lambda r: r["date"])
    result = []
    for i in range(1, len(months)):
        newer = months[i]
        older = months[i - 1]
        diff = {"month": newer["date"].strftime("%Y-%m")}
        for cat in CATEGORIES:
            diff[cat] = newer[cat] - older[cat]
        result.append(diff)
    return result


def totals_for_period(records, days=30):
    if len(records) < days + 1:
        days = len(records) - 1
    newest = records[0]
    oldest = records[days]
    result = {"from": oldest["date"], "to": newest["date"]}
    for cat in CATEGORIES:
        result[cat] = newest[cat] - oldest[cat]
    return result

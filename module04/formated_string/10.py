
from datetime import datetime

shop = "Silpo"
bought_at = datetime(2025, 4, 5, 18, 42)
items = [
    ("Bread", 1, 32.5),
    ("Milk 2.5%", 2, 41.9),
    ("Cheese", 0.35, 489.0),
    ("Coffee beans", 1, 1249.0),
]
discount = 0.05
width = 40


def receipt():
    lines = list()
    lines.append(f"{shop:^{width}}")
    lines.append(f"{bought_at:%d.%m.%Y %H:%M}".center(width))
    lines.append("=" * width)
    lines.append(f"{'Item':<16}{'Qty':>6}{'Price':>9}{'Sum':>9}")
    lines.append("-" * width)

    total = 0
    for title, qty, price in items:
        line_sum = qty * price
        total += line_sum
        lines.append(f"{title:<16}{qty:>6g}{price:>9.2f}{line_sum:>9.2f}")

    to_pay = total * (1 - discount)
    lines.append("-" * width)
    lines.append(f"{'Subtotal:':<30}{total:>10,.2f}")
    lines.append(f"{f'Discount ({discount:.0%}):':<30}{-total * discount:>10,.2f}")
    lines.append("=" * width)
    lines.append(f"{'TO PAY:':<30}{to_pay:>10,.2f}")
    lines.append(f"{'Thank you!':^{width}}")
    return lines


for line in receipt():
    print(line)

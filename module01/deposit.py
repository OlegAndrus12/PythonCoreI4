# Compound interest formula:
# Total = A * (1 + r) ^ t
# where:
# A = initial amount
# r = annual rate (decimal, e.g. 0.15 for 15%)
# t = time in years

import math

try:
    amount = float(input("Enter investment amount (UAH) >>> "))
    rate = float(input("Enter annual rate (%) >>> "))
    years = float(input("Enter term (years) >>> "))

    r = rate / 100

    total = math.floor(amount * math.pow(1 + r, years))
    income = total - amount

    print("Income =", income)
    print("Total =", total)

except ValueError:
    print("Error: please enter valid numbers")
except Exception as e:
    print("Unexpected error:", e)
# Leap year rules:
# divisible by 4       → leap year
# divisible by 100     → not a leap year
# divisible by 400     → leap year (overrides the 100 rule)
# Every 4 years is a leap year, except every 100 years — unless it's also divisible by 400.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

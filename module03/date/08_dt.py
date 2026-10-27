import calendar

# isleap — check if a year is a leap year
print(calendar.isleap(2024))  # True
print(calendar.isleap(2023))  # False

# monthrange — returns (weekday of 1st day, number of days in month)
# weekday: 0=Monday … 6=Sunday
first_weekday, num_days = calendar.monthrange(2024, 2)
print(f"Feb 2024 starts on weekday {first_weekday}, has {num_days} days")

# weekday — weekday index for a specific date (0=Mon, 6=Sun)
print(calendar.weekday(2024, 1, 1))  # Monday → 0

# iterating weeks of a month
for week in calendar.monthcalendar(2024, 2):
    print(week)  # 0 means the day belongs to another month

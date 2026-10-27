from datetime import date, timedelta

# Real life: HR / CRM. Age, next birthday, days to birthday.


def calculate_age(birth_date, today=None):
    today = today or date.today()
    # subtract 1 if this year's birthday has not happened yet
    before_birthday = (today.month, today.day) < (birth_date.month, birth_date.day)
    return today.year - birth_date.year - before_birthday


def birthdays_this_week(people, today=None):
    """Who has a birthday between Monday and Sunday of the current week?"""
    today = today or date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    print(monday, sunday)
    result = []
    for name, born in people.items():
        try:
            birthday = born.replace(year=today.year)
        except ValueError:  # born on 29 Feb, this year is not a leap year
            birthday = date(today.year, 3, 1)

        if monday <= birthday <= sunday:
            result.append((name, birthday, today.year - born.year))
    return sorted(result, key=lambda item: item[1])


today = date(2025, 4, 5)  # fixed date, so the output is always the same
birth = date(1990, 4, 20)

print(calculate_age(birth, today))  # 34: birthday is still ahead this year
print(calculate_age(date(1990, 4, 5), today))  # 35: birthday is today

# Team calendar: who has a birthday this week? (2025-04-05 is Saturday, week = 31 Mar - 6 Apr)
team = {
    "Anna": date(1992, 4, 6),
    "Petro": date(1988, 12, 1),
    "Olena": date(1995, 3, 31),
    "Ivan": date(1990, 4, 5),
}
for name, birthday, turns in birthdays_this_week(team, date.today()):
    print(f"{name}: {birthday.strftime('%A %d %b')}, turns {turns}")

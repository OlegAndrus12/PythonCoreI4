from datetime import datetime, date, time, timedelta

# datetime.combine — merge a date and a time into one datetime
d = date(2024, 6, 15)
t = time(9, 30, 0)
meeting = datetime.combine(d, t)
print(meeting)

# timedelta.total_seconds() — convert any duration to seconds
delta = timedelta(days=1, hours=2, minutes=30)
print(delta)
print(delta.total_seconds())  # 95400.0

# timedelta supports negative values (going back in time)
yesterday = datetime.now() - timedelta(days=1)
print(yesterday.date())

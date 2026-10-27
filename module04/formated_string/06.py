# Date formatting in f-strings
# datetime objects accept strftime codes right after the colon: f"{d:%Y-%m-%d}"

from datetime import date, datetime, timedelta

d = datetime(2025, 4, 5, 9, 7, 3)

# date parts
print(f"{d:%Y-%m-%d}")            # 2025-04-05  (ISO, sorts correctly)
print(f"{d:%d.%m.%Y}")            # 05.04.2025  (European style)
print(f"{d:%m/%d/%y}")            # 04/05/25    (US style, 2-digit year)

# time parts
print(f"{d:%H:%M}")               # 09:07       (24-hour)
print(f"{d:%H:%M:%S}")            # 09:07:03
print(f"{d:%I:%M %p}")            # 09:07 AM    (12-hour)

# names of days and months (English unless locale is changed)
print(f"{d:%A, %d %B %Y}")        # Saturday, 05 April 2025
print(f"{d:%a %d %b}")            # Sat 05 Apr

# day of year, week number, weekday number
print(f"{d:%j}")                  # 095  (day of year)
print(f"{d:%W}")                  # 13   (week number, Monday first)
print(f"{d:%w}")                  # 6    (weekday, Sunday = 0)

# works for date objects too (time codes give zeros)
today = date(2025, 12, 31)
print(f"Deadline: {today:%d.%m.%Y}")   # Deadline: 31.12.2025

# literal % inside a format → %%
print(f"{d:%d.%m — 100%% done}")  # 05.04 — 100% done

# format stored in a variable
fmt = "%Y/%m/%d %H:%M"
print(f"{d:{fmt}}")               # 2025/04/05 09:07

# no format spec → str(), = debug shortcut works too
print(f"{d}")                     # 2025-04-05 09:07:03
print(f"{d=}")                    # d=datetime.datetime(2025, 4, 5, 9, 7, 3)

# alignment: the spec after ':' goes to strftime, so format first, then align
print(f"|{d:%d.%m.%Y:>15}|")      # |05.04.2025:>15|  ← NOT aligned!
s = f"{d:%d.%m.%Y}"
print(f"|{s:>15}|")               # |     05.04.2025|

# timedelta has no format codes — build the string yourself
duration = timedelta(hours=2, minutes=5, seconds=30)
print(f"{duration}")              # 2:05:30
hours, rest = divmod(int(duration.total_seconds()), 3600)
minutes, seconds = divmod(rest, 60)
print(f"{hours:02d}h {minutes:02d}m {seconds:02d}s")   # 02h 05m 30s

# table of events
events = [
    ("Standup", datetime(2025, 4, 7, 9, 30)),
    ("Demo", datetime(2025, 4, 10, 15, 0)),
    ("Retro", datetime(2025, 4, 11, 16, 45)),
]
for title, when in events:
    day = f"{when:%a %d %b}"
    print(f"{title:<10}{day:<12}{when:%H:%M}")
# Standup   Mon 07 Apr  09:30
# Demo      Thu 10 Apr  15:00
# Retro     Fri 11 Apr  16:45

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# UTC = Coordinated Universal Time. The world's reference clock.
# - It is the same everywhere on Earth: no time zones, no daylight saving time (DST).
# - Every local time is UTC plus an offset: Kyiv is UTC+2 in winter, UTC+3 in summer.
# Rule: store and compare in UTC, convert to local time only when showing it to a person.

# 1. Current time in UTC
now = datetime.now(timezone.utc)
print(now)  # e.g. 2025-04-05 09:07:03.123456+00:00 (+00:00 = UTC)
print(now.tzinfo)  # UTC

# 2. Naive vs aware
naive = datetime.now()  # no zone attached, nobody knows which zone it is
print(naive.tzinfo)  # None
# datetime.utcnow() also returns a naive value, so use datetime.now(timezone.utc)

# 3. Create a fixed moment in UTC
created = datetime(2025, 4, 5, 9, 0, tzinfo=timezone.utc)
print(created.isoformat())  # 2025-04-05T09:00:00+00:00

# 4. Convert UTC to local time (for display only)
kyiv = created.astimezone(ZoneInfo("Europe/Kyiv"))
print(f"{kyiv:%Y-%m-%d %H:%M} {kyiv.tzname()}")  # 2025-04-05 12:00 EEST
texas = created.astimezone(ZoneInfo("America/Chicago"))
print(f"{texas:%Y-%m-%d %H:%M} {texas.tzname()}")  # 2025-04-05 04:00 CDT
print(kyiv == texas == created)  # True: same moment, three ways of writing it

# 5. Convert local time to UTC (e.g. before saving to a database)
local = datetime(2025, 4, 5, 16, 0, tzinfo=ZoneInfo("Europe/Kyiv"))
print(local.astimezone(timezone.utc))  # 2025-04-05 13:00:00+00:00

# 6. Any other zone: astimezone() takes any tzinfo, not only timezone.utc
plus3 = created.astimezone(timezone(timedelta(hours=3)))
print(f"{plus3:%Y-%m-%d %H:%M} {plus3.tzname()}")  # 2025-04-05 12:00 UTC+03:00
print(plus3 == created)  # True: same moment

winter = datetime(2025, 1, 15, 9, 0, tzinfo=timezone.utc)
print(winter.astimezone(timezone(timedelta(hours=3))))  # 2025-01-15 12:00:00+03:00 (wrong for Kyiv in winter)
print(winter.astimezone(ZoneInfo("Europe/Kyiv")))  # 2025-01-15 11:00:00+02:00 (correct)

# 8. Never mix naive and aware
try:
    print(created - naive)
except TypeError as error:
    print("TypeError:", error)

# 9. Handy: timestamps and "expires in 1 hour"
print(created.timestamp())  # seconds since 1970-01-01 00:00 UTC
print(created + timedelta(hours=1))  # 2025-04-05 10:00:00+00:00

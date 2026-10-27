from datetime import datetime
from zoneinfo import ZoneInfo  # stdlib since Python 3.9, no extra install

# attach timezone at creation
kyiv = ZoneInfo("Europe/Kyiv")
new_york = ZoneInfo("America/New_York")

now_kyiv = datetime.now(tz=kyiv)
now_ny = datetime.now(tz=new_york)

print("Kyiv:    ", now_kyiv)
print("New York:", now_ny)

# convert between zones — just call .astimezone()
converted = now_kyiv.astimezone(new_york)
print("Kyiv → NY:", converted)

# make a naive datetime timezone-aware
naive = datetime(2024, 6, 15, 12, 0, 0)
aware = naive.replace(tzinfo=kyiv)
print(aware)

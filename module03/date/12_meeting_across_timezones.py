from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Real life: a distributed team (Kyiv, Stockholm, Texas). Find a meeting time
# that is reasonable for everyone. ZoneInfo handles daylight saving time (DST).

OFFICES = {
    "Kyiv": ZoneInfo("Europe/Kyiv"),
    "Stockholm": ZoneInfo("Europe/Stockholm"),
    "Texas": ZoneInfo("America/Chicago"),
}


def show_meeting(start, label):
    print(f"--- {label}")
    for office, zone in OFFICES.items():
        local = start.astimezone(zone)
        print(f"{office:<10} {local:%a %d %b %H:%M} ({local.tzname()})")


# Rule: store and compare in UTC, convert to local time only for display.
meeting = datetime(2025, 4, 7, 16, 0, tzinfo=ZoneInfo("Europe/Kyiv"))
show_meeting(meeting, "Kyiv 16:00")

# Naive vs aware: never mix them
naive = datetime(2025, 4, 7, 12, 0)
aware = datetime(2025, 4, 7, 12, 0, tzinfo=OFFICES["Kyiv"])
try:
    print(aware - naive)
except TypeError as error:
    print("TypeError:", error)

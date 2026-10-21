from datetime import datetime
from zoneinfo import ZoneInfo

OFFICES = {
    "Kyiv": ZoneInfo("Europe/Kyiv"),
    "Stockholm": ZoneInfo("Europe/Stockholm"),
    "Texas": ZoneInfo("America/Chicago"),
}



for office, zone in OFFICES.items():
    now = datetime.today()
    print(office, now.astimezone(zone))
    
import json
import pathlib
from datetime import datetime

_DATA = pathlib.Path(__file__).parent / "moskali.json"

CATEGORIES = [
    "Особовий склад",
    "Танки",
    "ББМ",
    "Артилерійські системи",
    "РСЗВ",
    "Засоби ППО",
    "Літаки",
    "Гелікоптери",
    "БПЛА",
    "Крилаті ракети",
    "Кораблі (катери)",
    "Підводні човни",
    "Автомобілі та автоцистерни",
    "Спеціальна техніка",
]

LABELS = {
    "Особовий склад": "Personnel",
    "Танки": "Tanks",
    "ББМ": "Armored Vehicles",
    "Артилерійські системи": "Artillery",
    "РСЗВ": "MLRS",
    "Засоби ППО": "Air Defense",
    "Літаки": "Aircraft",
    "Гелікоптери": "Helicopters",
    "БПЛА": "UAVs/Drones",
    "Крилаті ракети": "Cruise Missiles",
    "Кораблі (катери)": "Ships/Boats",
    "Підводні човни": "Submarines",
    "Автомобілі та автоцистерни": "Vehicles & Trucks",
    "Спеціальна техніка": "Special Equipment",
}


def load():
    with open(_DATA, encoding="utf-8") as f:
        raw = json.load(f)
    records = []
    for r in raw:
        entry = {"date": datetime.fromisoformat(r["date"])}
        for cat in CATEGORIES:
            entry[cat] = int(r.get(cat, 0))
        records.append(entry)
    return records  # newest first

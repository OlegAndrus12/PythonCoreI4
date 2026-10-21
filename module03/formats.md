# Python `strftime` / `strptime` Format Codes

Reference date used in all examples: **Saturday, 05 April 2025, 09:07:03**

---

## Year

| Code | Description               | Example  |
|------|---------------------------|----------|
| `%Y` | Full 4-digit year         | `2025`   |
| `%y` | 2-digit year (00–99)      | `25`     |
| `%G` | ISO 8601 week-based year  | `2025`   |

---

## Month

| Code | Description                     | Example   |
|------|---------------------------------|-----------|
| `%m` | Month as zero-padded number     | `04`      |
| `%B` | Full month name                 | `April`   |
| `%b` | Abbreviated month name          | `Apr`     |

---

## Day

| Code | Description                              | Example |
|------|------------------------------------------|---------|
| `%d` | Day of month, zero-padded (01–31)        | `05`    |
| `%-d`| Day of month, no padding *(Unix only)*   | `5`     |
| `%j` | Day of year (001–366)                    | `095`   |

---

## Weekday

| Code | Description                        | Example    |
|------|------------------------------------|------------|
| `%A` | Full weekday name                  | `Saturday` |
| `%a` | Abbreviated weekday name           | `Sat`      |
| `%w` | Weekday as number (0=Sun, 6=Sat)   | `6`        |
| `%u` | Weekday as number (1=Mon, 7=Sun)   | `6`        |

---

## Hour

| Code | Description                        | Example |
|------|------------------------------------|---------|
| `%H` | Hour (24-hour clock), zero-padded  | `09`    |
| `%I` | Hour (12-hour clock), zero-padded  | `09`    |
| `%p` | AM or PM                           | `AM`    |

---

## Minute & Second

| Code | Description                      | Example |
|------|----------------------------------|---------|
| `%M` | Minute, zero-padded (00–59)      | `07`    |
| `%S` | Second, zero-padded (00–59)      | `03`    |
| `%f` | Microseconds, zero-padded (6 digits) | `000000` |

---

## Timezone

| Code | Description                          | Example            |
|------|--------------------------------------|--------------------|
| `%Z` | Timezone name                        | `UTC`, `EST`       |
| `%z` | UTC offset as `+HHMM` or `-HHMM`    | `+0200`            |

---

## Week Number

| Code | Description                                       | Example |
|------|---------------------------------------------------|---------|
| `%W` | Week number of year, Monday as first day (00–53)  | `13`    |
| `%U` | Week number of year, Sunday as first day (00–53)  | `14`    |
| `%V` | ISO 8601 week number (01–53)                      | `14`    |

---

## Composite Codes (shortcuts)

| Code | Equivalent          | Example                     |
|------|---------------------|-----------------------------|
| `%c` | Full locale datetime | `Sat Apr  5 09:07:03 2025` |
| `%x` | Locale date          | `04/05/25`                 |
| `%X` | Locale time          | `09:07:03`                 |
| `%%` | Literal `%` sign     | `%`                        |

---

## Common Format Patterns

```python
from datetime import datetime

dt = datetime(2025, 4, 5, 9, 7, 3)

dt.strftime("%Y-%m-%d")               # 2025-04-05        (ISO date)
dt.strftime("%d/%m/%Y")               # 05/04/2025        (EU style)
dt.strftime("%m/%d/%Y")               # 04/05/2025        (US style)
dt.strftime("%d %B %Y")               # 05 April 2025
dt.strftime("%A, %d %B %Y")           # Saturday, 05 April 2025
dt.strftime("%H:%M:%S")               # 09:07:03
dt.strftime("%I:%M %p")               # 09:07 AM
dt.strftime("%Y-%m-%d %H:%M:%S")      # 2025-04-05 09:07:03
dt.strftime("%d-%m-%Y %H:%M")         # 05-04-2025 09:07
```

---

## Parsing with `strptime`

```python
from datetime import datetime

datetime.strptime("05-04-2025", "%d-%m-%Y")
datetime.strptime("2025/04/05 09:07", "%Y/%m/%d %H:%M")
datetime.strptime("Saturday, 05 April 2025", "%A, %d %B %Y")
datetime.strptime("05 Apr 25", "%d %b %y")
datetime.strptime("09:07:03 AM", "%I:%M:%S %p")
```

import re
from pathlib import Path

LOGS = Path(__file__).parent / "logs.txt"



# [02/Jun/2025 15:05:03] WARNING [django.security] ... - 10.0.0.2
LINE_RE = re.compile(
    r"\s(?P<level>\w+)"                         # \s — space before level; \w+ — word chars (ERROR/WARNING/INFO)
    r"\s\[(?P<module>[^\]]+)\]"                 # \[ \] — literal brackets; [^\]]+ — anything that isn't ]
    r".+(?P<ip>\d{1,3}(?:\.\d{1,3}){3})$"     # .+? — lazy skip of message; \d{1,3} — octet; {3} — repeat 3x; $ — end of line
)

counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
errors_by_ip = {}

with open(LOGS) as f:
    for line in f:
        m = LINE_RE.search(line.strip())
        if not m:
            continue

        level  = m.group("level")
        module = m.group("module")
        ip     = m.group("ip")

        counts[level] = counts.get(level, 0) + 1

        if level == "ERROR":
            errors_by_ip[ip] = errors_by_ip.get(ip, 0) + 1

total = sum(counts.values())

print("=== Log level summary ===")
for level, count in counts.items():
    bar = "#" * count
    print(f"  {level:<10} {count:>3}  {bar}")
print(f"\n  Total lines: {total}")

print("\n=== Top IPs by error count ===")
top_ips = sorted(errors_by_ip.items(), key=lambda x: x[1], reverse=True)
for ip, count in top_ips:
    print(f"  {ip:<18} {count} errors")

from datetime import datetime

# Real life: DevOps / support. Parse timestamps from a log, measure durations,
# group events by hour.

LOG = """\
2025-04-05 09:07:03 INFO  Service started
2025-04-05 09:07:41 ERROR Database timeout
2025-04-05 09:15:10 INFO  Retry succeeded
2025-04-05 10:02:55 ERROR Payment gateway 502
2025-04-05 10:03:20 ERROR Payment gateway 502
2025-04-05 11:45:00 INFO  Deploy finished
"""

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_LENGTH = 19  # len("2025-04-05 09:07:03")


def report(log):
    for line in log.splitlines():
        moment = datetime.strptime(line[:TIME_LENGTH], TIME_FORMAT)
        level, _, message = line[TIME_LENGTH:].strip().partition(" ")
        # ISO for machines, readable for people
        print(moment.isoformat(), "|", moment.strftime("%d %B %Y, %I:%M %p"), "|", level, message.strip())


report(LOG)

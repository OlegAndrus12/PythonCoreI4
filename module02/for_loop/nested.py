# Nested loops — generate a weekly class schedule
days = ["Mon", "Tue", "Wed", "Thu"]
periods = ["9:00", "11:00", "13:00", "15:00"]

print("\nWeekly schedule slots:")
for day in days:
    for time in periods:
        print(f"  {day} {time}")

# Nested loops — check every player against every other for a round-robin tournament
players = ["Alice", "Bob", "Charlie", "Diana"]

print("\nRound-robin matchups:")
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"  {players[i]} vs {players[j]}")

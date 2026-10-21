import random

# random.choice — picks ONE item (no replacement)
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))

# random.sample — picks k UNIQUE items (no replacement)
# unlike choices(), duplicates are impossible
lottery = list(range(1, 50))
ticket = random.sample(lottery, k=6)
print(sorted(ticket))

# contrast with choices() which CAN repeat
with_repeats = random.choices(lottery, k=6)
print(sorted(with_repeats))

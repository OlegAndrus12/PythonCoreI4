import random

# random.random() — float in [0.0, 1.0)
print(random.random())

# random.uniform(a, b) — float in [a, b]
temperature = random.uniform(-10.0, 35.0)
print(f"{temperature:.2f}")

# random.seed() — fix the seed for reproducible results
random.seed(42)
print([random.randint(1, 100) for _ in range(5)])

random.seed(42)
print([random.randint(1, 100) for _ in range(5)])  # identical output

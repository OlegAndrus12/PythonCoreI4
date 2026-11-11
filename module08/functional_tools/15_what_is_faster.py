# Loop vs comprehension vs map/filter — which is faster?

from time import perf_counter

LIMIT = 1_000_000


def timed(label, func):
    start = perf_counter()
    func()
    print(f"{label:<40} {(perf_counter() - start) * 1000:.1f} ms")


# --- Transform: squares -----------------------------------------------------
def squares_loop():
    squares = []
    for i in range(LIMIT):
        squares.append(i**2)
    return squares


timed("for loop squares", squares_loop)
timed("list comprehension squares", lambda: [i**2 for i in range(LIMIT)])
# map is lazy — without list() nothing is computed and the timing lies
timed("map + lambda squares (lazy, unevaluated)", lambda: map(lambda i: i**2, range(LIMIT)))
timed("map + lambda squares", lambda: list(map(lambda i: i**2, range(LIMIT))))


# --- Select: even numbers ---------------------------------------------------
def evens_loop():
    evens = []
    for i in range(LIMIT):
        if i % 2 == 0:
            evens.append(i)
    return evens


timed("for loop evens", evens_loop)
timed("list comprehension evens", lambda: [i for i in range(LIMIT) if i % 2 == 0])
timed("filter + lambda evens", lambda: list(filter(lambda i: i % 2 == 0, range(LIMIT))))

# Takeaway: comprehensions are usually fastest for inline logic;
# map/filter + lambda pay for a Python function call per element.

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper


# --- using @ ---
@timer
def fetch_users():
    time.sleep(0.3)  # simulate DB query
    return ["Alice", "Bob", "Carol"]


# --- calling directly ---
def generate_report(users):
    time.sleep(0.2)  # simulate file write
    return f"Report for {len(users)} users"

generate_report = timer(generate_report)


if __name__ == "__main__":
    users = fetch_users()
    report = generate_report(users)
    print(report)

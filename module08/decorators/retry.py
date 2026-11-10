import time
import random
from functools import wraps


def retry(times=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"[{func.__name__}] attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


def flaky_api_call():
    if random.random() < 0.7:
        raise ConnectionError("Service unavailable")
    return {"status": "ok", "data": [1, 2, 3]}


@retry(times=5, delay=0.5, exceptions=(ConnectionError,))
def fetch_orders():
    return flaky_api_call()


if __name__ == "__main__":
    result = fetch_orders()
    print("Got:", result)

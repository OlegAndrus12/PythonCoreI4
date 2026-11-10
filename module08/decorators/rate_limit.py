import time
from functools import wraps


def rate_limit(max_calls, period=1.0):
    def decorator(func):
        window_start = 0.0
        call_count = 0

        # @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal window_start, call_count
            now = time.time()
            if now - window_start >= period:
                window_start = now
                call_count = 0
            if call_count >= max_calls:
                remaining = period - (now - window_start)
                print(f"[{time.strftime('%H:%M:%S')}] DENIED — limit of {max_calls} calls reached, resets in {remaining:.0f}s")
                return
            call_count += 1
            return func(*args, **kwargs)

        return wrapper
    return decorator


@rate_limit(max_calls=5, period=10)
def send_sms(phone, message):
    print(f"[{time.strftime('%H:%M:%S')}] Sending to {phone}...")
    time.sleep(0.1)
    print(f"[{time.strftime('%H:%M:%S')}] Sent: {message}")


if __name__ == "__main__":
    i = 0
    while True:
        send_sms(f"+38055332321", "Your order has been shipped.")
        i += 1
        time.sleep(1)

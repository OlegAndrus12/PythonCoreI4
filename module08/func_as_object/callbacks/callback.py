import random


def fetch_payment(payment_id, on_success, on_error):
    if random.random() > 0.4:
        on_success({"id": payment_id, "status": "completed", "amount": 250.00})
    else:
        on_error({"id": payment_id, "code": 503, "reason": "Gateway timeout"})


def handle_success(payment):
    print(f"[OK]  Payment #{payment['id']} of ${payment['amount']} confirmed.")


def handle_error(error):
    print(f"[ERR] Payment #{error['id']} failed [{error['code']}]: {error['reason']}")


for pid in range(1001, 1006):
    fetch_payment(pid, on_success=handle_success, on_error=handle_error)

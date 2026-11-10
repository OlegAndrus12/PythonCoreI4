def send_email(user, message):
    print(f"[EMAIL] To: {user['email']} | {message}")


def send_sms(user, message):
    print(f"[SMS]   To: {user['phone']} | {message}")


def send_push(user, message):
    print(f"[PUSH]  To: {user['device_id']} | {message}")


CHANNELS = {
    "email": send_email,
    "sms": send_sms,
    "push": send_push,
}


def notify(user, message, channel="email"):
    handler = CHANNELS.get(channel)
    if not handler:
        raise ValueError(f"Unknown channel: {channel!r}")
    handler(user, message)


user = {
    "email": "alice@example.com",
    "phone": "+380991234567",
    "device_id": "abc123",
}

notify(user, "Your order has been shipped!", channel="email")
notify(user, "Your order has been shipped!", channel="sms")
notify(user, "Your order has been shipped!", channel="push")

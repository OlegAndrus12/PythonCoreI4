class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


def send_confirmation(order):
    print(f"[EMAIL] Order #{order['id']} confirmed → {order['email']}")


def reserve_stock(order):
    print(f"[INVENTORY] Reserving stock for order #{order['id']}")


def charge_card(order):
    print(f"[PAYMENT] Charging ${order['total']} for order #{order['id']}")


emitter = EventEmitter()
emitter.on("order.placed", send_confirmation)
emitter.on("order.placed", reserve_stock)
emitter.on("order.placed", charge_card)

emitter.emit("order.placed", {"id": 1042, "email": "bob@example.com", "total": 149.99})

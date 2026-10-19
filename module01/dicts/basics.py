# --- 1. User profile ---
user = {
    "name": "Alice",
    "age": 28,
    "email": "alice@example.com",
    "city": "Kyiv",
}

print(user["name"])           # Alice
print(user.get("phone"))      # None — key doesn't exist, no crash
print(user.get("phone", "n/a"))  # n/a — safe default

# update a single field
user["city"] = "Lviv"
print(user["city"]) # Lviv

# add a new field
user["phone"] = "+380501234567"
print(user)

# --- 2. Product in an online store ---
product = {
    "title": "Wireless Mouse",
    "price": 499.00,
    "currency": "UAH",
    "in_stock": True,
    "rating": 4.7,
}

# read specific fields
print(product["title"], product["price"], product["currency"])

# price went up
product["price"] = 549.00
print(product["price"])

# remove a field we no longer need
product.pop("rating")
print(product)

# --- 3. HTTP response from an API ---
response = {
    "status": 200,
    "ok": True,
    "data": {
        "user_id": 42,
        "username": "bob",
        "token": "abc123",
    },
}

# nested access
print(response["status"])             # 200
print(response["data"]["username"])   # bob
print(response["data"]["token"])      # abc123


# --- 4. Config / settings ---
config = {
    "host": "localhost",
    "port": 5432,
    "db_name": "myapp",
    "debug": True,
}

# override defaults for production
prod_overrides = {"host": "db.prod.example.com", "debug": False}
config.update(prod_overrides)
print(config)

# inspect what keys and values are available
print(config.keys())    # dict_keys(['host', 'port', 'db_name', 'debug'])
print(config.values())  # dict_values([...])


# --- 5. What can be used as a dict key ---

# A key must be hashable — its value must never change after creation.
# Immutable types (str, int, float, bool, tuple) are hashable → valid keys.
# Mutable types (list, dict, set) are not hashable → TypeError.

# str — most common key
labels = {"title": "Imagine", "artist": "John Lennon"}

# int — e.g. HTTP status codes mapped to messages
status_messages = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
}
print(status_messages[404])   # Not Found

# float — rare but valid (avoid: rounding errors make lookups fragile)
thresholds = {0.5: "medium", 1.0: "high"}

# bool — valid (True == 1 and False == 0, so they collide with int keys)
flags = {True: "enabled", False: "disabled"}
print(flags[True])    # enabled

# tuple — composite key, useful when identity depends on multiple fields

# Exchange rates: direction matters — (from, to) is the key
exchange_rates = {
    ("USD", "EUR"): 0.92,
    ("USD", "UAH"): 41.5,
    ("EUR", "UAH"): 45.1,
    ("EUR", "USD"): 1.08,
}
print(exchange_rates[("USD", "UAH")])   # 41.5
print(exchange_rates[("EUR", "USD")])   # 1.08

# Config per environment: (service, env) → config value
configs = {
    ("db", "dev"):  "localhost:5432",
    ("db", "prod"): "db.prod.example.com:5432",
    ("cache", "dev"):  "localhost:6379",
    ("cache", "prod"): "redis.prod.example.com:6379",
}
print(configs[("db", "prod")])      # db.prod.example.com:5432
print(configs[("cache", "dev")])    # localhost:6379

# City coordinates: (lat, lon) tuple as a key
landmarks = {
    (50.4501, 30.5234): "Kyiv",
    (48.8566, 2.3522):  "Paris",
    (51.5074, -0.1278): "London",
}
print(landmarks[(48.8566, 2.3522)])   # Paris

# list as key → TypeError
try:
    bad = {["A", 1]: "Alice"}
except TypeError as e:
    print(e)   # unhashable type: 'list'


# --- KeyError ---

# Accessing a missing key with [] raises KeyError
try:
    print(user["phone"])
except KeyError:
    print("Key not found")

# Safe alternatives
print(user.get("phone"))           # None — no crash
print(user.get("phone", "n/a"))    # "n/a" — explicit fallback

# Check before accessing
if "phone" in user:
    print(user["phone"])

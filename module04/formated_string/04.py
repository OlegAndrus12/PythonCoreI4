# f-string power features

name = "Oleh"
price = 49.95

# = debug shortcut (Python 3.8+): prints "name=value"
x = 42
print(f"{x=}")           # x=42
print(f"{price=:.2f}")   # price=49.95


# multiline f-string
person = {"name": "Oleh", "age": 25}
card = (
    f"Name : {person['name']}\n"
    f"Age  : {person['age']}\n"
    f"Adult: {person['age'] >= 18}"
)
print(card)

# conditional inside f-string
score = 73
print(f"Result: {'pass' if score >= 60 else 'fail'}")

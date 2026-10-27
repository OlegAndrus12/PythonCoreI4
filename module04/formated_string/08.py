# Older formatting styles: % operator and str.format()
# f-strings are the default today, but you will meet these in existing code

name = "Oleh"
age = 25
price = 49.95

# % operator (printf-style, the oldest)
print("%s is %d years old" % (name, age))      # Oleh is 25 years old
print("Price: %.2f" % price)                    # Price: 49.95
print("|%10s|%-10s|" % (name, name))            # |      Oleh|Oleh      |
print("%05d" % 42)                              # 00042
print("Progress: %d%%" % 80)                    # Progress: 80%
print("%(name)s, %(age)d" % {"name": name, "age": age})   # Oleh, 25


# str.format()
print("{} is {} years old".format(name, age))          # Oleh is 25 years old
print("{0} {1} {0}".format("ha", "hi"))                # ha hi ha       ← by index
print("{n} is {a}".format(n=name, a=age))              # Oleh is 25     ← by name
print("Price: {:.2f}".format(price))                   # Price: 49.95   ← same spec as f-strings

# main advantage: the template can be stored and reused
template = "Dear {name}, your order #{order:05d} is ready"
orders = [
    {"name": "Oleh", "order": 17},
    {"name": "Iryna", "order": 128},
]
for order in orders:
    print(template.format(**order))
    
# Dear Oleh, your order #00017 is ready
# Dear Iryna, your order #00128 is ready


# same result, three styles
print("%s: %.1f%%" % (name, 76.4))
print("{}: {:.1f}%".format(name, 76.4))
print(f"{name}: {76.4:.1f}%")
# Oleh: 76.4%  (x3)

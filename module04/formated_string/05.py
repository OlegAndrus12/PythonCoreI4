# Number formatting in f-strings

n = 1234567.891

# thousands separator
print(f"{n:,.2f}")        # 1,234,567.89
print(f"{n:_.2f}")        # 1_234_567.89

# fixed-point precision
print(f"{n:.0f}")         # 1234568
print(f"{n:.4f}")         # 1234567.8910

# scientific notation
print(f"{n:e}")           # 1.234568e+06
print(f"{n:.2e}")         # 1.23e+06

# sign: always show + or -
print(f"{42:+d}")         # +42
print(f"{-42:+d}")        # -42

# zero-padding with width
print(f"{7:05d}")         # 00007

# integer bases
num = 255
print(f"{num:b}")         # 11111111  (binary)
print(f"{num:o}")         # 377       (octal)
print(f"{num:x}")         # ff        (hex lower)
print(f"{num:X}")         # FF        (hex upper)
print(f"{num:#x}")        # 0xff      (with prefix)

# percentage
ratio = 0.764
print(f"{ratio:.1%}")     # 76.4%

person = {"name": "Oleh", "age": 25}
print(f"Name: {person["name"]}")  # Name: Oleh   (before 3.12 → SyntaxError)

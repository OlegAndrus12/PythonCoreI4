number = int(input("Enter a number: "))

n = number
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(f"Sum of digits of {number}: {total}")


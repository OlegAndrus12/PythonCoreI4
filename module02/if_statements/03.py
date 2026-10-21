# and — both conditions must be true
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("Access granted.")
else:
    print("Access denied.")

# or — at least one condition must be true
is_weekend = input("Is it a weekend? (yes/no): ") == "yes"
is_holiday = input("Is it a holiday? (yes/no): ") == "yes"

if is_weekend or is_holiday:
    print("The store is closed.")
else:
    print("The store is open.")

# not — inverts the condition
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue.")

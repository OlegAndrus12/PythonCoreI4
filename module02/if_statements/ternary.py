# ternary operator: <value_if_true> if <condition> else <value_if_false>

age = int(input("Enter your age: "))
status = "adult" if age >= 18 else "minor"
print(status)

# assigning role based on IP
ip = input("Enter IP: ")
role = "admin" if ip == "129.12.12.12" else "user"
print(f"Role: {role}")

# inline label for a test result
score = int(input("Enter score: "))
result = "passed" if score >= 60 else "failed"
print(f"Exam {result}")

# in — check membership in a list
role = input("Enter your role: ")

if role in ["admin", "moderator"]:
    print("You can delete posts.")
else:
    print("You don't have permission.")

# not in — opposite of in
banned_users = ["john_doe", "spam_bot", "hacker99"]
username = input("Enter username: ")

if username not in banned_users:
    print("Welcome!")
else:
    print("Your account is banned.")

# chained comparison — cleaner than using and
score = int(input("Enter score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")
elif 75 <= score < 90:
    print("Grade: B")
elif 60 <= score < 75:
    print("Grade: C")
else:
    print("Grade: F")

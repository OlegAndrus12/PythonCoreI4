# Iterating over a list — printing installed dependencies
dependencies = ["requests", "flask", "sqlalchemy", "pydantic", "uvicorn"]

print("Installed packages:")
for package in dependencies:
    print(f"  - {package}")

# Iterating over a string — reading each character of a file extension
filename = "report.csv"
print("\nCharacters in filename:")
for char in filename:
    print(char, end=" ")
print()

# Iterating with range — simulating line numbers when reading a file
lines = [
    "import os",
    "import sys",
    "",
    "path = os.getcwd()",
    "print(path)",
]

print("\nFile contents:")
for line_number in range(len(lines)):
    print(f"{line_number + 1} | {lines[line_number]}")

# range with step — sampling every 100th request from a server log
total_requests = 1000
print("\nSampled request IDs (every 100th):")
for request_id in range(0, total_requests, 100):
    print(f"  Request #{request_id}")

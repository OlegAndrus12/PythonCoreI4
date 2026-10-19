# Extract all .py filenames from a directory listing
all_files = ["main.py", "README.md", "utils.py", ".env", "models.py", "config.yaml"]
python_files = []

for f in all_files:
    if f.endswith(".py"):
        python_files.append(f)

print(f"Python files: {python_files}")

# Keep only failed HTTP responses
responses = [200, 404, 200, 500, 301, 403, 200, 502]
errors = []

for code in responses:
    if code >= 400:
        errors.append(code)

print(f"\nError responses: {errors}")

# Uppercase all environment variable names
raw_env = ["database_url", "secret_key", "debug", "allowed_hosts"]
env_vars = []

for var in raw_env:
    env_vars.append(var.upper())

print(f"\nEnv variable names: {env_vars}")

# Build a package → version lookup from a requirements list
requirements = [
    "requests==2.31.0",
    "flask==3.0.1",
    "sqlalchemy==2.0.20",
    "pydantic==2.5.3",
]

packages = {}
for line in requirements:
    name, version = line.split("==")
    packages[name] = version

print("\nInstalled versions:")
for name, version in packages.items():
    print(f"  {name}: {version}")

# Count occurrences of each log level in a log file
log_entries = ["INFO", "WARNING", "INFO", "ERROR", "INFO", "CRITICAL", "ERROR", "INFO"]
level_counts = {}

for level in log_entries:
    if level not in level_counts:
        level_counts[level] = 0
    level_counts[level] += 1

print("\nLog level counts:")
for level, count in sorted(level_counts.items()):
    print(f"  {level}: {count}")

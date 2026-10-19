
config_lines = [
    "# database settings",
    "DB_HOST=localhost",
    "DB_PORT=5432",
    "# app settings",
    "DEBUG=True",
    "PORT=8000",
]

configs = {}

print("Parsed configs")
for line in config_lines:
    if line.startswith("#"):
        continue

    name, value = line.split("=")
    configs[name] = value

print(configs)
# break — scan log lines and stop at the first CRITICAL error
log_lines = [
    "INFO: server started on port 8000",
    "INFO: connected to database",
    "WARNING: slow query detected (320ms)",
    "CRITICAL: out of memory — process killed",
    "ERROR: failed to restart service",
]

print("Scanning logs:")
for line in log_lines:
    print(f"  {line}")
    if line.startswith("CRITICAL"):
        print("  >>> CRITICAL error found. Stopping scan.")
        break

# continue — parse a config file, skip comments and blank lines
config_lines = [
    "# database settings",
    "DB_HOST=localhost",
    "DB_PORT=5432",
    "# app settings",
    "DEBUG=True",
    "PORT=8000",
]

print("\nParsed config:")
for line in config_lines:
    if line.startswith("#"):
        continue
    key, value = line.split("=")
    print(f"  {key.strip()} → {value.strip()}")

# break + continue — process a deployment queue:
# skip already deployed, stop on a broken build
queue = [
    {"service": "user-service", "state": "pending"},
    {"service": "payment-service", "state": "broken"},
    {"service": "notification-service", "state": "pending"},
]

print("\nDeployment queue:")
for item in queue:
    if item["state"] == "deployed":
        print(f"  {item['service']} — already deployed, skipping.")
        continue
    if item["state"] == "broken":
        print(f"  {item['service']} — broken build! Halting deployment.")
        break
    print(f"  {item['service']} — deploying...")

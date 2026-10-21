print("=== Dragon Quest ===")

while True:
    print("\n1 — New Game")
    print("2 — Load Game")
    print("3 — Settings")
    print("0 — Quit")

    choice = input("\nChoose an option: ")

    if choice == "0":
        print("See you next time, hero!")
        break

    if choice not in ("1", "2", "3"):
        print("Unknown command, try again.")
        continue

    if choice == "1":
        name = input("Enter your hero's name: ")
        print(f"\nWelcome, {name}! Your adventure begins...")
    elif choice == "2":
        slot = input("Enter save slot (1-3): ")
        print(f"Loading save slot {slot}...")
    elif choice == "3":
        print("Settings: [sound: ON] [fullscreen: OFF]")

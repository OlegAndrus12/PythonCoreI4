from enum import Enum


class MenuOption(Enum):
    NEW_GAME = "1"
    LOAD_GAME = "2"
    SETTINGS = "3"
    QUIT = "0"


print("=== Dragon Quest ===")

while True:
    print("\n1 — New Game")
    print("2 — Load Game")
    print("3 — Settings")
    print("0 — Quit")

    choice = input("\nChoose an option: ")

    try:
        option = MenuOption(choice)
    except ValueError:
        print("Unknown command, try again.")
        continue

    match option:
        case MenuOption.QUIT:
            print("See you next time, hero!")
            break
        case MenuOption.NEW_GAME:
            name = input("Enter your hero's name: ")
            print(f"\nWelcome, {name}! Your adventure begins...")
        case MenuOption.LOAD_GAME:
            slot = input("Enter save slot (1-3): ")
            print(f"Loading save slot {slot}...")
        case MenuOption.SETTINGS:
            print("Settings: [sound: ON] [fullscreen: OFF]")

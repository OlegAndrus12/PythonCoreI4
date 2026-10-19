song = "bohemian rhapsody"
artist = "Queen"
plays = 1_200_000

# --- Formatting ---

# Old style
print("Now playing: %s by %s" % (song, artist))

# .format()
print("Now playing: {} by {}".format(song, artist))

# f-string (preferred)
print(f"Now playing: {song} by {artist} — {plays:,} plays")

# Multiline string (e.g. lyrics snippet)
lyrics = """
Is this the real life?
Is this just fantasy?
"""
print(lyrics)


# --- Case methods ---

print(song.upper())       # BOHEMIAN RHAPSODY
print(song.lower())       # bohemian rhapsody
print(song.title())       # Bohemian Rhapsody
print(song.capitalize())  # Bohemian rhapsody
print(song.swapcase())    # BOHEMIAN RHAPSODY → bohemian rhapsody


# --- Search & check ---

print("rhapsody" in song)           # True
print(song.startswith("bohemian"))  # True
print(song.endswith("rhapsody"))    # True
print(song.find("rhapsody"))        # 9 — index of first match, -1 if not found
print(song.count("a"))              # count occurrences of a character


# --- Modify ---

messy = "  Stairway to Heaven   "
print(messy.strip())                        # remove surrounding whitespace
print(song.replace("rhapsody", "medley"))   # Bohemian medley
print(song.title().replace(" ", "_"))       # Bohemian_Rhapsody (slug-style)


# --- Split & join ---

tags = "rock,classic,guitar,epic"
tag_list = tags.split(",")           # ['rock', 'classic', 'guitar', 'epic']
print(tag_list)

print(" | ".join(tag_list))          # rock | classic | guitar | epic


# --- Slicing ---

title = "Bohemian Rhapsody"
print(title[:8])     # Bohemian
print(title[9:])     # Rhapsody
print(title[::-1])   # reversed


# --- IndexError ---

# Accessing a character at an out-of-range index raises IndexError
try:
    print(title[100])
except IndexError:
    print("No character at that position")

# Safe alternatives
print(title[0] if title else "")   # guard against empty string too
print(title[:1])                   # slicing never raises — returns "" if out of range

# ============================================================
# Tuples — ordered, immutable sequences
# ============================================================

# --- Creating ---

track = ("Bohemian Rhapsody", "Queen", 1975)   # (title, artist, year)
single = ("Imagine",)                           # single-element tuple — trailing comma is required
empty = ()

print(type(track))    # <class 'tuple'>
print(type(single))   # <class 'tuple'>
print(type("Imagine"))# <class 'str'>  ← no comma = just a string, not a tuple


# --- Accessing ---

print(track[0])       # Bohemian Rhapsody
print(track[-1])      # 1975
print(track[1:])      # ('Queen', 1975)


# --- Unpacking ---

title, artist, year = track
print(title)          # Bohemian Rhapsody
print(artist)         # Queen
print(year)           # 1975

# Swap two variables without a temp variable
a, b = "Imagine", "Black"
a, b = b, a
print(a, b)           # Black  Imagine

# Ignore values you don't need with _
_, artist, _ = track
print(artist)         # Queen

# Extended unpacking — first track, rest of the playlist
first, *rest = ("Imagine", "Black", "Wonderwall", "Hotel California")
print(first)          # Imagine
print(rest)           # ['Black', 'Wonderwall', 'Hotel California']


# --- Immutability ---

# Tuples cannot be modified after creation
try:
    track[0] = "Another One Bites the Dust"
except TypeError as e:
    print(e)          # 'tuple' object does not support item assignment


# --- Methods ---

playlist = ("Imagine", "Black", "Wonderwall", "Imagine", "Black", "Imagine")

print(playlist.count("Imagine"))   # 3 — how many times it appears
print(playlist.index("Black"))     # 1 — position of first match

# IndexError if out of range — same as lists
try:
    print(playlist[100])
except IndexError:
    print("No track at that position")


# --- Tuple vs list ---

# Use a tuple when data should not change — e.g. a track's metadata
track_meta = ("Bohemian Rhapsody", "Queen", 5, 55)  # title, artist, min, sec

# Use a list when you need to add/remove items — e.g. a queue
queue = ["Imagine", "Black"]
queue.append("Wonderwall")


# --- Tuples as dict keys (lists cannot be used as keys) ---

chart_positions = {
    ("Bohemian Rhapsody", "Queen"): 1,
    ("Imagine", "John Lennon"): 2,
    ("Black", "Pearl Jam"): 3,
}

print(chart_positions[("Imagine", "John Lennon")])  # 2



# ============================================================
# Real-life use cases for tuples
# ============================================================


# --- 1. Coordinates / location (data that shouldn't change) ---

# GPS coordinates of a venue — latitude and longitude are a natural pair
kyiv = (50.4501, 30.5234)
london = (51.5074, -0.1278)

def distance_label(origin, destination):
    return f"From {origin} to {destination}"

print(distance_label(kyiv, london))


# --- 2. Returning multiple values from a function ---

# Python functions can only return one object — a tuple lets you return several
def parse_track(raw):
    parts = raw.split(" - ")
    return parts[0].strip(), parts[1].strip()   # returns a tuple

title, artist = parse_track("Bohemian Rhapsody - Queen")
print(title)    # Bohemian Rhapsody
print(artist)   # Queen


# --- 3. Unpacking API / CSV data row by row ---

# Imagine each row from a CSV or API response is a fixed-structure record
tracks = [
    ("Bohemian Rhapsody", "Queen", 1975, 354),
    ("Imagine", "John Lennon", 1971, 187),
    ("Black", "Pearl Jam", 1991, 344),
]

for title, artist, year, duration_sec in tracks:
    minutes, seconds = divmod(duration_sec, 60)
    print(f"{title} by {artist} ({year}) — {minutes}:{seconds:02d}")


# --- 4. Dict keys — grouping by a composite key ---

# A tuple can be a dict key; a list cannot
monthly_plays = {
    ("Bohemian Rhapsody", "January"): 84_000,
    ("Bohemian Rhapsody", "February"): 91_000,
    ("Imagine", "January"): 60_000,
}

print(monthly_plays[("Bohemian Rhapsody", "February")])  # 91000


# --- 5. Tuples in sets — deduplicating composite records ---

# Lists are unhashable and can't be stored in a set; tuples can
played_pairs = {
    ("Bohemian Rhapsody", "Queen"),
    ("Imagine", "John Lennon"),
    ("Bohemian Rhapsody", "Queen"),   # duplicate — silently ignored
}

print(len(played_pairs))   # 2

# Practical: track which (user, song) pairs have already been scrobbled
scrobbled = set()

def scrobble(user, track):
    key = (user, track)
    if key in scrobbled:
        print(f"Already scrobbled: {track}")
        return
    scrobbled.add(key)
    print(f"Scrobbled '{track}' for {user}")

scrobble("alice", "Imagine")        # Scrobbled
scrobble("alice", "Imagine")        # Already scrobbled
scrobble("bob",   "Imagine")        # Scrobbled — different user


# --- 6. Swap without a temp variable ---

now_playing = "Imagine"
up_next = "Black"

now_playing, up_next = up_next, now_playing
print(now_playing)   # Black
print(up_next)       # Imagine


# --- 7. Fixed-size config / constants ---

# App settings that must never change at runtime
SUPPORTED_FORMATS = ("mp3", "flac", "wav", "aac")
DEFAULT_VOLUME = (0, 100, 50)   # min, max, default

def validate_format(fmt):
    if fmt not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {fmt}. Allowed: {SUPPORTED_FORMATS}")

validate_format("mp3")   # ok
try:
    validate_format("exe")
except ValueError as e:
    print(e)


# --- 8. Grouping function arguments (used in sorting, min/max) ---

# When sorting by multiple criteria, tuples define priority
tracks = [
    ("Imagine", "John Lennon", 1971),
    ("Black", "Pearl Jam", 1991),
    ("Imagine", "A Perfect Circle", 2003),
]

# Sort by title first, then by artist — comparison works element by element
tracks.sort(key=lambda t: (t[0], t[1]))
for t in tracks:
    print(t)

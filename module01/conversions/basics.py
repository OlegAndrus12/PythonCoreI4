# ============================================================
# Type Conversions
# ============================================================


# --- int ---

plays = 1200000

print(float(plays))       # 1200000.0
print(bool(plays))        # True  (0 → False, anything else → True)
print(str(plays))         # "1200000"


# --- float ---

rating = 4.8

print(int(rating))        # 4  (truncates, does not round)
print(bool(rating))       # True  (0.0 → False, anything else → True)
print(str(rating))        # "4.8"


# --- bool ---

is_playing = True

print(int(is_playing))    # 1  (False → 0)
print(float(is_playing))  # 1.0
print(str(is_playing))    # "True"


# --- None ---

current_track = None

print(bool(current_track))   # False  (None is always falsy)
print(str(current_track))    # "None"
# int(None) and float(None) raise TypeError


# --- str ---

plays_str = "3500"
rating_str = "4.8"
track = "Bohemian Rhapsody"

print(int(plays_str))         # 3500
print(float(rating_str))      # 4.8
print(bool(track))            # True  (empty string "" → False)
print(list(track))            # ['B','o','h','e','m','i','a','n',' ','R',...]
# int("4.8") raises ValueError — must go through float first
print(int(float(rating_str))) # 4


# --- list ---

playlist = ["Imagine", "Black", "Wonderwall", "Imagine"]

print(set(playlist))          # {'Imagine', 'Black', 'Wonderwall'}  — deduped, unordered
print(tuple(playlist))        # ('Imagine', 'Black', 'Wonderwall', 'Imagine')
print(", ".join(playlist))    # "Imagine, Black, Wonderwall, Imagine"
print(bool(playlist))         # True  (empty list [] → False)


# --- set ---

unique_tracks = {"Imagine", "Black", "Wonderwall"}

print(list(unique_tracks))    # order not guaranteed
print(tuple(unique_tracks))   # order not guaranteed
print(bool(unique_tracks))    # True  (empty set set() → False)
# dict(unique_tracks) raises TypeError — sets have no key-value pairs


# --- dict ---

track_info = {"title": "Imagine", "artist": "John Lennon", "year": 1971}

print(list(track_info))       # ['title', 'artist', 'year']  — keys only
print(list(track_info.values()))   # ['Imagine', 'John Lennon', 1971]
print(list(track_info.items()))    # [('title', 'Imagine'), ...]
print(bool(track_info))       # True  (empty dict {} → False)
print(str(track_info))        # string repr — useful for logging, not parsing


# --- Chained / practical conversions ---

# User input always comes as str — convert before use
user_input = "5"
stars = int(user_input) * "★"
print(stars)                  # ★★★★★

# Deduplicate a playlist and sort it
raw = ["Imagine", "Black", "Imagine", "Wonderwall", "Black"]
deduped = sorted(list(set(raw)))
print(deduped)                # ['Black', 'Imagine', 'Wonderwall']

# Build a comma-separated tag string from a set
genres = {"rock", "classic", "psychedelic"}
print(", ".join(sorted(genres)))  # classic, psychedelic, rock

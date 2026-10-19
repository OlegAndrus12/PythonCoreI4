playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]

# Add a new track to the end
playlist.append("Wonderwall")

# How many times is a song duplicated?
print(playlist.count("Stairway to Heaven"))  # 2

# Find position of a song
print(playlist.index("Imagine"))  # 4

# Reverse play order (last added plays first)
playlist.reverse()

# Remove one duplicate
playlist.remove("Stairway to Heaven")

# Merge with another playlist (e.g. a friend's picks)
friends_picks = ["Come As You Are", "Black"]
playlist.extend(friends_picks)

# Insert an urgent track at position 0 (play next)
playlist.insert(0, "Let It Be")

# Sort alphabetically
playlist.sort()
playlist.sort(reverse=True)

# Sort by track name length
playlist.sort(key=len)

print(playlist)

# --- Slicing ---

# First 3 tracks (opening set)
print(playlist[:3])

# Last 3 tracks (closing set)
print(playlist[-3:])

# Tracks 2–5
print(playlist[1:5])

# Every other track (odd positions)
print(playlist[::2])

# Reverse the playlist without mutating it
print(playlist[::-1])

# Copy the playlist
playlist_copy = playlist[:]

# Clear playlist
playlist.clear()

# --- IndexError ---

tracks = ["Imagine", "Black", "Wonderwall"]

# Accessing an index that doesn't exist raises IndexError
try:
    print(tracks[10])
except IndexError:
    print("No track at that position")

# Safe alternatives
print(tracks[2] if len(tracks) > 2 else "No track")  # index guard
print(next(iter(tracks), None))                        # first item or None if empty

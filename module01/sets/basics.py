# --- Basic operations ---

liked_songs = {"Bohemian Rhapsody", "Imagine", "Hotel California", "Smells Like Teen Spirit"}

liked_songs.add("Wonderwall")
print("Wonderwall" in liked_songs)  # True

# remove() raises KeyError if missing, discard() does not
liked_songs.remove("Wonderwall")
liked_songs.discard("Wonderwall")  # safe — no error even if already removed


# --- Deduplication ---

# Converting playlists with duplicates to sets removes repeated tracks
playlist_monday = ["Imagine", "Black", "Wonderwall", "Imagine", "Hotel California", "Black"]
playlist_friday = ["Black", "Wonderwall", "Come As You Are", "Wonderwall", "Smells Like Teen Spirit"]

set_monday = set(playlist_monday)
set_friday = set(playlist_friday)


# --- Set operations ---

alice_likes = {"Bohemian Rhapsody", "Stairway to Heaven", "Imagine", "Black"}
bob_likes = {"Imagine", "Black", "Wonderwall", "Come As You Are"}

# All unique songs both users like (union)
print(alice_likes | bob_likes)

# Songs liked by both (intersection)
print(alice_likes & bob_likes)

# Songs only Alice likes — recommendations for Bob (difference)
print(alice_likes - bob_likes)

# Songs liked by only one of them, not both (symmetric difference)
print(alice_likes ^ bob_likes)

# Do they share any songs at all?
print(alice_likes.isdisjoint(bob_likes))  # False

# Is bob's taste a subset of alice's?
print(bob_likes.issubset(alice_likes))  # False

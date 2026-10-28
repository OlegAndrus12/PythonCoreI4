# Practice 07 — Instagram content moderator
#
# Instagram wants to auto-moderate posts before publishing.
# Replace every banned word (case-insensitive) with asterisks
# matching the word's length.
#
# Examples:
#   post = "This is a damn good photo, holy shit!"
#   banned = ["damn", "shit"]
#   → "This is a **** good photo, holy ****!"
#
#   post = "What the hell is going on?!"
#   banned = ["hell"]
#   → "What the **** is going on?!"
#
# Hints:
#   - str.replace / str.lower for matching
#   - "*" * len(word) to build the mask
#   - keep original casing of the surrounding text intact


BAD_WORDS = ["damn", "shit", "hell", "crap", "ass"]


def moderate(post, banned=BAD_WORDS):
    """
    Replace each banned word in post with asterisks (case-insensitive, whole-word only).

    Works by keeping a lowercased shadow of the string for searching while
    rebuilding the original-cased result in sync. Whole-word boundaries are
    checked with isalpha() so substrings inside longer words are left intact
    (e.g. 'class' is not affected by a ban on 'ass').
    """
    result = post
    lower = result.lower()
    for word in banned:
        mask = "*" * len(word)
        start = 0
        while True:
            idx = lower.find(word, start)
            if idx == -1:
                break
            
            before_ok = idx == 0 or not lower[idx - 1].isalpha()
            after_ok = idx + len(word) == len(lower) or not lower[idx + len(word)].isalpha()

            if before_ok and after_ok:
                result = result[:idx] + mask + result[idx + len(word):]
                lower = lower[:idx] + mask + lower[idx + len(word):]
            start = idx + len(word)

    return result


posts = [
    "This is a damn good photo, holy shit!",
    "What the hell is going on?!",
    "Great day, no bad words here.",
    "[DAMN] this view is unreal!!",
]

for post in posts:
    print(f"original : {post}")
    print(f"moderated: {moderate(post)}")
    print()

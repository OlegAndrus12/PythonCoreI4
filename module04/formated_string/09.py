# String alignment methods: ljust, rjust, center, zfill
# same job as the format spec, but as str methods

word = "Python"

print(f"|{word.ljust(10)}|")        # |Python    |
print(f"|{word.rjust(10)}|")        # |    Python|
print(f"|{word.center(10)}|")       # |  Python  |

# custom fill character (exactly one char)
print(word.ljust(10, "."))          # Python....
print(word.center(12, "*"))         # ***Python***

# string longer than width → returned unchanged, never cut
print(word.ljust(3))                # Python

# zfill: pad with zeros on the left, keeps the sign in front
print("42".zfill(5))                # 00042
print("-42".zfill(5))               # -0042
print(str(7).zfill(3))              # 007

# same results with format spec
print(f"|{word:<10}|{word:>10}|{word:^10}|")   # |Python    |    Python|  Python  |
print(f"{42:05d}")                             # 00042

# practical: table of contents
chapters = [("Introduction", 1), ("Data types", 7), ("Functions", 23)]
for title, page in chapters:
    print(title.ljust(20, ".") + str(page).rjust(4, "."))
# Introduction...........1
# Data types.............7
# Functions.............23

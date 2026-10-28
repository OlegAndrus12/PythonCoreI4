import re

caption = "Loving the #sunset view in #Kyiv! Shoutout to @john_doe and @travel.gram for the inspo!"

hashtags = re.findall(r"#\w+", caption)
mentions = re.findall(r"@[\w.]+", caption)
print("Hashtags:", hashtags)
print("Mentions:", mentions)

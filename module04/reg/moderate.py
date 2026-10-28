import re

def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)


def replace_spam_words(text, spam_words):
    pattern = rf"\b({'|'.join(spam_words)})\b"
    return re.sub(pattern, lambda m: "*" * len(m.group()), text, flags=re.IGNORECASE)

text = " to be or not to be an [idiot]. BE a good coder!"
# try without be / ignore
res = re.findall(r"\bbe\b", text, flags=re.IGNORECASE)
print(res)


res = replace_spam_words(text, ["idiot", "coder"])
print(res)
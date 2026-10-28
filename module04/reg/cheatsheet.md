# Python Regex Cheatsheet

## `re` module functions

| Function | Returns | Description |
|---|---|---|
| `re.match(pat, s)` | Match or None | Match at the **start** of string |
| `re.search(pat, s)` | Match or None | First match **anywhere** in string |
| `re.findall(pat, s)` | list of strings | All non-overlapping matches |
| `re.finditer(pat, s)` | iterator of Match | All matches as Match objects |
| `re.sub(pat, repl, s)` | string | Replace all matches |
| `re.split(pat, s)` | list | Split string on matches |
| `re.compile(pat)` | Pattern | Pre-compile for reuse |

```python
import re

re.search(r"\d+", "abc 42")       # <Match '42'>
re.findall(r"\d+", "1 and 2")     # ['1', '2']
re.sub(r"\d+", "#", "a1 b2")      # 'a# b#'
re.split(r"\s+", "a b  c")        # ['a', 'b', 'c']
```

---

## Character classes

| Symbol | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` | Digit `[0-9]` |
| `\D` | Non-digit |
| `\w` | Word character `[a-zA-Z0-9_]` |
| `\W` | Non-word character |
| `\s` | Whitespace (space, tab, newline…) |
| `\S` | Non-whitespace |

```python
re.findall(r"\d+", "price: 49.99")      # ['49', '99']
re.findall(r"\w+", "hello, world!")     # ['hello', 'world']
re.sub(r"\s+", " ", "a  b   c")        # 'a b c'
re.sub(r"\D", "", "+38 (067) 123")     # '38067123'  ← strip non-digits
```

---

## Custom character sets `[...]`

| Pattern | Matches |
|---|---|
| `[abc]` | a, b, or c |
| `[^abc]` | anything except a, b, c |
| `[a-z]` | lowercase letter |
| `[A-Za-z0-9]` | letter or digit |
| `[aeiou]` | vowels |

```python
re.findall(r"[aeiou]+", "beautiful")    # ['eau', 'i', 'u']
re.sub(r"[^a-z0-9]", "-", "Hello!")    # '-ello-'
re.findall(r"[A-Z]+", "NASA and CIA")  # ['NASA', 'CIA']
```

---

## Anchors

| Symbol | Matches |
|---|---|
| `^` | Start of string (or line with `re.M`) |
| `$` | End of string (or line with `re.M`) |
| `\b` | Word boundary |
| `\B` | Non-word boundary |
| `\A` | Absolute start of string |
| `\Z` | Absolute end of string |

```python
re.findall(r"^\d+", "42 items")         # ['42']  ← only if at start
re.findall(r"\bcat\b", "cat concatenate")  # ['cat']  ← whole word only
re.findall(r"\d+$", "total: 100")       # ['100']
```

---

## Quantifiers

| Symbol | Meaning |
|---|---|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | Between n and m |

```python
re.findall(r"\d{4}", "2026-04-28")      # ['2026']
re.findall(r"\d{1,2}", "day: 4, month: 28")  # ['4', '28']
re.findall(r"colou?r", "color colour") # ['color', 'colour']
re.findall(r"\w+@\w+\.\w+", "a@b.com") # ['a@b.com']
```

### Greedy vs lazy

By default quantifiers are **greedy** (match as much as possible).  
Add `?` to make them **lazy** (match as little as possible).

```python
s = "<b>bold</b> and <i>italic</i>"

re.findall(r"<.+>", s)    # ['<b>bold</b> and <i>italic</i>']  ← greedy
re.findall(r"<.+?>", s)   # ['<b>', '</b>', '<i>', '</i>']      ← lazy
```

---

## Groups `(...)`

| Pattern | Description |
|---|---|
| `(abc)` | Capturing group |
| `(?:abc)` | Non-capturing group |
| `(?P<name>abc)` | Named capturing group |
| `(?P=name)` | Backreference to named group |
| `\1`, `\2` | Backreference by index |

```python
# capturing group — .group(1)
m = re.search(r"(\w+)@(\w+)\.(\w+)", "user@gmail.com")
m.groups()          # ('user', 'gmail', 'com')
m.group(1)          # 'user'

# named groups — .groupdict()
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "2026-04-28")
m.groupdict()       # {'year': '2026', 'month': '04', 'day': '28'}

# non-capturing — group not returned
re.findall(r"(?:Mr|Ms)\.?\s(\w+)", "Mr. Smith and Ms Jones")  # ['Smith', 'Jones']

# backreference — match repeated word
re.search(r"\b(\w+)\s+\1\b", "the the error")  # matches 'the the'
```

---

## Alternation `|`

```python
re.findall(r"cat|dog", "I have a cat and a dog")   # ['cat', 'dog']
re.findall(r"\b(jpg|png|gif)\b", "photo.jpg logo.png")  # ['jpg', 'png']
```

---

## Lookahead & lookbehind

| Pattern | Description |
|---|---|
| `(?=...)` | Positive lookahead — what follows |
| `(?!...)` | Negative lookahead — what does NOT follow |
| `(?<=...)` | Positive lookbehind — what precedes |
| `(?<!...)` | Negative lookbehind — what does NOT precede |

```python
# price followed by USD only
re.findall(r"\d+(?= USD)", "100 USD and 50 EUR")    # ['100']

# digits NOT preceded by $
re.findall(r"(?<!\$)\d+", "item $10 code 42")       # ['42']

# word NOT followed by ing
re.findall(r"\b\w+(?!ing)\b", "running jumping fly") # filters out -ing forms
```

---

## Flags

| Flag | Short | Description |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Case-insensitive matching |
| `re.MULTILINE` | `re.M` | `^`/`$` match each line |
| `re.DOTALL` | `re.S` | `.` matches newline too |
| `re.VERBOSE` | `re.X` | Allow whitespace/comments in pattern |

```python
re.findall(r"error", "ERROR found", re.I)          # ['ERROR']

text = "line1\nline2\nline3"
re.findall(r"^\w+", text, re.M)                    # ['line1', 'line2', 'line3']

re.search(r"start.+end", "start\nend", re.S)       # matches across newline

pattern = re.compile(r"""
    \d{4}   # year
    -
    \d{2}   # month
    -
    \d{2}   # day
""", re.X)
pattern.findall("date: 2026-04-28")                # ['2026-04-28']
```

---

## `re.sub` with a function

```python
# double every number found
re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b2 c10")  # 'a2 b4 c20'

# mask bad words
words = ["damn", "hell"]
pat = rf"\b({'|'.join(words)})\b"
re.sub(pat, lambda m: "*" * len(m.group()), "damn it to hell", flags=re.I)
# '**** it to ****'
```

---

## Escape sequences summary

| Sequence | Meaning |
|---|---|
| `\.` | Literal dot |
| `\*` | Literal asterisk |
| `\(` `\)` | Literal parentheses |
| `\\` | Literal backslash |

Always use **raw strings** `r"..."` for patterns to avoid double-escaping:
```python
re.search(r"\d+", s)    # correct
re.search("\\d+", s)    # same but harder to read
```

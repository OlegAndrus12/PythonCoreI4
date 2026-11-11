# map / filter vs list comprehensions

## Quick comparison

| | `map` / `filter` | list comprehension |
|---|---|---|
| Returns | lazy iterator | list |
| Readability | good when reusing a named function | better for inline logic |
| Performance | slightly faster with named functions | faster with inline expressions |
| Chaining | easy to chain | nesting gets messy |
| Debugging | harder (lazy, no intermediate list) | easier (already a list) |

---

## map

```python
# map with named function — preferred when the function already exists
result = list(map(str.upper, words))

# equivalent comprehension — preferred for inline transforms
result = [w.upper() for w in words]
```

**Use `map` when:** passing a named function (`str.strip`, `int`, `abs`, your own function).  
**Use comprehension when:** the transform is a short inline expression.

---

## filter

```python
# filter with named function
result = list(filter(is_valid, items))

# equivalent comprehension
result = [x for x in items if is_valid(x)]
```

**Use `filter` when:** passing a named predicate function.  
**Use comprehension when:** the condition is inline and you want to read it as English ("give me x for x in items if ...").

---

## Chaining

```python
# map + filter chained — readable left-to-right
result = list(filter(lambda x: x > 10, map(lambda x: x ** 2, numbers)))

# comprehension — all in one line, easier to parse
result = [x ** 2 for x in numbers if x ** 2 > 10]

# even cleaner with an intermediate variable
squared = (x ** 2 for x in numbers)          # generator, lazy
result = [x for x in squared if x > 10]
```

---

## When to use each

### Prefer `map` / `filter`
- You already have a named function (`map(int, strings)`, `filter(str.strip, lines)`)
- You want lazy evaluation (processing large streams without building a list)
- You're composing pipelines and chaining multiple steps

### Prefer list comprehensions
- The logic is short and inline
- You need a list immediately (not a lazy iterator)
- Readability matters more than composability
- You have a condition AND a transform (`[f(x) for x in xs if pred(x)]`)

### Avoid
- Lambdas inside `map`/`filter` when a comprehension reads better
- Nested `map(map(...))` — use a comprehension or a named function instead
- Comprehensions longer than one line — extract into a named function

---

## any / all cheat sheet

```python
# any: True if at least one element is truthy
any(x > 0 for x in numbers)          # is there a positive number?
any("admin" in roles for roles in users)

# all: True only if every element is truthy
all(x > 0 for x in numbers)          # are all numbers positive?
all(field in form for field in required)
```

**Short-circuit:** `any` stops at the first `True`; `all` stops at the first `False`.  
Use generator expressions (not list comprehensions) inside `any`/`all` to keep this benefit.

```python
# good — short-circuits
any(is_valid(x) for x in items)

# bad — builds the whole list first, no short-circuit
any([is_valid(x) for x in items])
```

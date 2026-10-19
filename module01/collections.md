# Python Data Structures — Comparison

| Feature              | `list`           | `tuple`          | `set`            | `dict`                  | `str`            |
|----------------------|------------------|------------------|------------------|-------------------------|------------------|
| **Syntax**           | `[1, 2, 3]`      | `(1, 2, 3)`      | `{1, 2, 3}`      | `{"k": "v"}`            | `"hello"`        |
| **Ordered**          | Yes              | Yes              | No               | Yes (insertion, 3.7+)   | Yes              |
| **Mutable**          | Yes              | No               | Yes              | Yes                     | No               |
| **Duplicates**       | Yes              | Yes              | No               | Keys: No / Values: Yes  | Yes              |
| **Indexed access**   | By index         | By index         | No               | By key                  | By index         |
| **Hashable**         | No               | Yes (if items are)| No              | No                      | Yes              |
| **Common use**       | Ordered items    | Fixed records    | Unique items     | Key-value mapping       | Text             |
| **Sortable in-place**| Yes              | No               | No               | No                      | No               |

## Time Complexity

| Operation            | `list`  | `tuple` | `set`   | `dict`  | `str`   |
|----------------------|---------|---------|---------|---------|---------|
| **Access by index**  | O(1)    | O(1)    | —       | O(1)    | O(1)    |
| **Search (`in`)**    | O(n)    | O(n)    | O(1)    | O(1)    | O(n)    |
| **Append / Add**     | O(1)    | —       | O(1)    | O(1)    | —       |
| **Insert at index**  | O(n)    | —       | —       | —       | —       |
| **Delete**           | O(n)    | —       | O(1)    | O(1)    | —       |
| **Iteration**        | O(n)    | O(n)    | O(n)    | O(n)    | O(n)    |

## Key Rules

- **list** — go-to for ordered, changeable sequences
- **tuple** — use when data should not change (coordinates, DB rows, dict keys)
- **set** — deduplication, membership tests, set math (`|`, `&`, `-`, `^`)
- **dict** — key-value lookup; keys must be hashable (str, int, tuple — yes; list — no)
- **str** — immutable sequence of characters; supports most sequence operations

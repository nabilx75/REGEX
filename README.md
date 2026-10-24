# Python Regular Expressions (Regex) Sheet

Regular expressions (regex) are patterns used to search, match, and extract text.

In Python, use the `re` module:

```python
import re
```

## 1. Character Classes

A character class uses square brackets `[]` to match **one character** from a set of allowed characters.

| Pattern | Meaning | Example matches |
|---|---|---|
| `[abc]` | One character: `a`, `b`, or `c` | `a`, `b`, `c` |
| `[cbr]at` | `cat`, `bat`, or `rat` | `cat`, `bat`, `rat` |
| `[0-9]` | One digit from 0 to 9 | `3`, `7` |
| `[A-Z]` | One uppercase English letter | `A`, `M` |
| `[a-z]` | One lowercase English letter | `a`, `x` |
| `[.!?]` | One of `.`, `!`, or `?` | `.`, `!`, `?` |

Example:

```python
text = "cat bat rat dog"
print(re.findall(r"[cbr]at", text))
```

Output:

```text
['cat', 'bat', 'rat']
```

`[cbr]` matches exactly one of the characters `c`, `b`, or `r`. The following `at` must match literally.

### Negated Character Classes: `[^...]`

When `^` appears **at the beginning of a character class**, it means **NOT**.

- `[.!?]` matches one period, exclamation mark, or question mark.
- `[^.!?]` matches any one character except `.`, `!`, or `?`.

For example, `[^.!?]+` matches one or more characters that are not sentence-ending punctuation.

> Note: `^` has a different meaning outside a character class: it usually marks the beginning of a string or line.

## 2. Quantifiers

Quantifiers specify how many times the **preceding character or pattern** may occur.

| Symbol | Meaning | Example |
|---|---|---|
| `*` | Zero or more | `ab*` matches `a`, `ab`, `abb` |
| `+` | One or more | `\d+` matches `7`, `42`, `123` |
| `?` | Zero or one (optional) | `colou?r` matches `color` and `colour` |
| `{3}` | Exactly three | `\d{3}` matches `123` |
| `{2,4}` | Between two and four | `\d{2,4}` matches `12`, `123`, `1234` |

### Important: `+` does not mean “digits” by itself

- `+` means **one or more repetitions of the preceding pattern**.
- `\d` means **one digit**.
- `\d+` means **one or more digits**.

Example:

```python
text = "cat123 dog45 bird7"
print(re.findall(r"\d+", text))
```

Output:

```text
['123', '45', '7']
```

## 3. Common Special Sequences

| Pattern | Meaning |
|---|---|
| `\d` | A digit (in Python, generally any Unicode decimal digit) |
| `\w` | A word character: typically a letter, digit, or underscore |
| `\s` | A whitespace character, such as a space, tab, or newline |
| `\b` | A word boundary, such as the boundary between a word character and a non-word character |

Examples:

```python
text = "cat 123"
print(re.findall(r"\d", text))   # ['1', '2', '3']
print(re.findall(r"\w+", text))  # ['cat', '123']
print(re.findall(r"\s", text))   # [' ']
```

Use a raw string such as `r"\d+"` for regex patterns in Python. The `r` helps Python treat backslashes as part of the pattern.

## 4. Alternation: `|`

The pipe symbol `|` means **OR**. It lets a pattern match one alternative or another.

```python
text = "cat123 dog123 bird456"
print(re.findall(r"(cat|dog)123", text))
```

Output:

```text
['cat', 'dog']
```

The parentheses `()` create a **capturing group**. Because the group is captured, `findall()` returns only the captured text (`cat` and `dog`) rather than the entire match.

### Non-Capturing Groups: `(?:...)`

Use `(?:...)` when you want to group alternatives without capturing the group.

```python
text = "cat123 dog123 bird456"
print(re.findall(r"(?:cat|dog)123", text))
```

Output:

```text
['cat123', 'dog123']
```

Here, `(?:cat|dog)` means “match `cat` or `dog`, but do not capture that group.” As a result, `findall()` returns each full match.

## 5. Quick Summary

- `[]` defines a character class and matches one character from the class.
- `[^...]` matches one character **not** listed in the class.
- `*` means zero or more repetitions.
- `+` means one or more repetitions.
- `?` means zero or one repetition.
- `{3}` means exactly three repetitions.
- `{2,4}` means between two and four repetitions.
- `\d` matches a digit; `\d+` matches one or more digits.
- `\w` matches a word character.
- `\s` matches whitespace.
- `\b` marks a word boundary.
- `(cat|dog)` groups alternatives and captures the chosen alternative.
- `(?:cat|dog)` groups alternatives without capturing them.

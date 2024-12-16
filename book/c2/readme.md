# c2: Pure Python Optimizations

Optimizations via better algorithms and data structures.

## 1 using the right algorithms and data structures

Better algos & data structures can efficiently help us scale our applications. Let's review the *Big O notation* some built-in data types in Python:

Just run the scripts to view the average time consumed, for eg.:

```bash
python .\book\c2\lists.py
```

### Lists

| Method | Time |
| --- | --- |
| `list.pop()` | O(1) |
| `list.pop(0)` | O(N) |
| `list.append(1)` | O(1) |
| `list.insert(0, 1)` | O(N) |

### Deques

Lists might not be efficient for insertion or removal both at the beginning and the end of the collection. We use `collections.deque` (*deque* stands for **double-ended queue**).



###

## 2 improving efficiency with caching and memoization

## 3 efficient iterating with comprehensions and generators

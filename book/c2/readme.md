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

### Deque

Lists might not be efficient for insertion or removal both at the beginning and the end of the collection. We use `collections.deque` (*deque* stands for **double-ended queue**).

`pop()` and `popleft()` will remove the last (on the right) and the fist (on the left) of the deque with time complexity `O(1)`. Similar for appending operations. But this comes with a cost, accessing the middle element of the deque will require `O(N)` time.

The searching operation in a list normally requires 'O(N)' (with `list.index`). A simple way to speed up is using `bisect.bisect` (module `collection`).

| Method | Time |
| --- | --- |
| `deque.pop()` | O(1) |
| `deque.popleft()` | O(1) |
| `deque.append()` | O(1) |
| `deque.appendleft()` | O(1) |
| `deque[0]` | O(1) |
| `deque[N-1]` | O(1) |
| `deque[int(N / 2)]` | O(N) |
| `list.index(a)` | O(N) |
| `index_bisect(list, a)` | O(log(N)) |

### Dictionaries

Dictionaries are widely used in Python including objects (packages, modules, classes) namespaces and annotations. They're implemented as **hash maps** and performing well with insertion, deletion, accessing with O(1) time complexity on average.

A typical (advanced) use case of dictionaries/hash maps is efficiently counting unique elements in a list. This pattern is wrapped in Python module named `collections`. Below wecan see all these methods have the same time complexity, but the `Counter()` is most efficient - check by run the `dictionaries.py`:

| Method | Time |
| --- | --- |
| `Counter(items)` | O(N) |
| `counter_dict(items)` | O(N) |
| `counter_defaultdict(items)` | O(N) |

Another

### Sets

### Heaps

### Trees

## 2 improving efficiency with caching and memoization

## 3 efficient iterating with comprehensions and generators

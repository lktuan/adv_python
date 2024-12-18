from bisect import bisect_left

from utils import print_scaling

if __name__ == "__main__":
    print_scaling(
        "collection.pop()",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection.popleft()",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection.append(1)",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection.appendleft(1)",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection[0]",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection[{N} - 1]",
        setup="from collections import deque; collection = deque(range({N}))",
    )

    print_scaling(
        "collection[int({N}/2)]",
        setup="from collections import deque; collection = deque(range({N}))",
    )
    setup_code = """
import random
random.seed(42)
collection = list(range({N}))
"""
    print_scaling("collection.index(random.randint(0, {N}))", setup=setup_code)

    def index_bisect(a, x):
        "Locate the leftmost value exactly equal to x"
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    setup_code = """
from __main__ import index_bisect

import random
random.seed(42)

collection = list(range({N}))
"""

    print_scaling("index_bisect(collection, random.randint(0, {N}))", setup=setup_code)

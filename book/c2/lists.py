from bisect import bisect_left

from utils import *

if __name__ == "__main__":

    print_scaling("collection.pop()", setup="collection = list(range({N}))")
    print_scaling("collection.pop(0)", setup="collection = list(range({N}))")
    print_scaling("collection.append(1)", setup="collection = list(range({N}))")
    print_scaling("collection.insert(0, 1)", setup="collection = list(range({N}))")
    print_scaling("collection.insert(5000, 1)", setup="collection = list(range({N}))")
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

# This cell contains some utility functions to prepare and execute the benchmarks
import timeit
from collections import defaultdict
from random import choice
from string import ascii_uppercase


def random_string(length):
    """Produce a random string made of *length* uppercase ascii characters"""
    return "".join(choice(ascii_uppercase) for i in range(length))


def print_scaling(stmt, setup, sizes=[10000, 20000, 30000], repeat=False, units="us"):
    """Print scaling information for the statement *stmt*, executed after *setup*.

    The *setup* and *stmt* arguments take a template string where "{N}"
    will be replaced as the size of the input.

    The *repeat* flags determined if the setup needs to be run between
    each test run.
    """
    values = []
    for size in sizes:
        if repeat:
            timings = timeit.repeat(
                stmt.format(N=size), setup=setup.format(N=size), number=1, repeat=1000
            )
            values.append(min(timings))
        else:
            timings = timeit.repeat(
                stmt.format(N=size), setup=setup.format(N=size), number=1000, repeat=3
            )
            values.append(min(t / 1000 for t in timings))
    unit_factor = {"us": 1e6, "ms": 1e3}[units]

    print(
        stmt,
        ": ",
        " | ".join(
            "N = {} t = {:.2f} ({})".format(n, t * unit_factor, units)
            for n, t in zip(sizes, values)
        ),
    )


def counter_defaultdict(items):
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return counter


def counter_dict(items):
    counter = {}
    for item in items:
        if item not in counter:
            counter[item] = 0
        else:
            counter[item] += 1
    return counter

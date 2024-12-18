from utils import print_scaling

if __name__ == "__main__":
    setup_code = """
from utils import random_string
collection = {{random_string(16) : i for i in range({N})}}
"""

    print_scaling('"ITEM" in collection', setup=setup_code, sizes=[1000, 2000, 3000])

    print_scaling(
        'collection["ITEM"] if "ITEM" in collection else None',
        setup=setup_code,
        sizes=[1000, 2000, 3000],
    )

    print_scaling('collection["ITEM"] = 0', setup=setup_code, sizes=[1000, 2000, 3000])

    setup_code = """
from utils import random_string
collection = {{random_string(16) : i for i in range({N})}}
"""

    print_scaling(
        '"X"  * {N} in collection', setup=setup_code, sizes=[1000, 2000, 3000]
    )

    setup_code = """
from uuid import uuid4
from collections import Counter
from utils import counter_defaultdict, counter_dict
import random

random.seed(42)
collection = [random.randint(0, 100) for i in range({N})]
"""

    print_scaling("Counter(collection)", setup=setup_code, sizes=[1000, 2000, 3000])

    print_scaling(
        "counter_defaultdict(collection)", setup=setup_code, sizes=[1000, 2000, 3000]
    )

    print_scaling(
        "counter_dict(collection)", setup=setup_code, sizes=[1000, 2000, 3000]
    )

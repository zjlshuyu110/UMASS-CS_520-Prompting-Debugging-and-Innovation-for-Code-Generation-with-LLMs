from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold <= 0 or len(numbers) < 2:
        return False

    buckets = {}
    t = threshold
    for x in numbers:
        if math.isnan(x):
            continue
        # duplicates (incl. inf==inf) immediately satisfy for t>0
        if x in buckets.get("dups", set()):
            return True
        # handle infinities as a special duplicate set
        if math.isinf(x):
            buckets.setdefault("dups", set()).add(x)
            continue

        k = math.floor(x / t)
        for key in (k - 1, k, k + 1):
            if key in buckets:
                y = buckets[key]
                if abs(x - y) < t:
                    return True
        buckets[k] = x
    return False

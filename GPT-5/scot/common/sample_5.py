from typing import List, Any
import bisect

def common(l1: list, l2: list):
    """
    Sort l2 once, then for each unique element of l1, binary-search in l2.
    Collect hits uniquely and return sorted.
    """
    if not l1 or not l2:
        return []

    b = sorted(l2)
    result = set()
    for x in set(l1):  # iterate unique candidates from l1
        idx = bisect.bisect_left(b, x)
        if idx < len(b) and b[idx] == x:
            result.add(x)
    return sorted(result)

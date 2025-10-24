from typing import List, Any

def common(l1: list, l2: list):
    """
    Build a membership set from the smaller list, collect matches uniquely,
    and return them sorted.
    """
    if len(l1) <= len(l2):
        small, large = l1, l2
    else:
        small, large = l2, l1

    small_set = set(small)
    hits = set()
    for x in large:
        if x in small_set:
            hits.add(x)

    return sorted(hits)

from typing import List, Any

def common(l1: list, l2: list):
    """
    Return a sorted list of unique elements present in both l1 and l2.
    """
    return sorted(set(l1).intersection(l2))

from typing import List, Any
from collections import Counter

def common(l1: list, l2: list):
    """
    Use Counter intersection to identify elements that appear in both,
    then return sorted unique keys of the intersection.
    """
    inter = Counter(l1) & Counter(l2)
    return sorted(inter.keys())

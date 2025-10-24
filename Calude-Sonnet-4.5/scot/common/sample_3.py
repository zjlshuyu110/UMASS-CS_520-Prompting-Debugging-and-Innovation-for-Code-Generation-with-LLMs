def common(l1: list, l2: list):
    """Find common elements using list comprehension and set for O(1) lookup."""
    set2 = set(l2)
    return sorted(list(set(x for x in l1 if x in set2)))
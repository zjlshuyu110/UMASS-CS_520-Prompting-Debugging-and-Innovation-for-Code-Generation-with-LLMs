def common(l1: list, l2: list):
    """Find common elements using filter()."""
    set2 = set(l2)
    return sorted(list(set(filter(lambda x: x in set2, l1))))
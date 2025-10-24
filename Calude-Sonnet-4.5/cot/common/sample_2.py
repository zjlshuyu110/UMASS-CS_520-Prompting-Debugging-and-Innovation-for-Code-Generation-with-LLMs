def common(l1: list, l2: list):
    """Return sorted list of unique elements present in both lists."""
    set2 = set(l2)
    return sorted({item for item in l1 if item in set2})
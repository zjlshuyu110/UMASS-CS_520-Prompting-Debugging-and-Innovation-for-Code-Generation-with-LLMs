def common(l1: list, l2: list):
    """Return a sorted list of unique elements common to both lists."""
    return sorted(set(l1) & set(l2))

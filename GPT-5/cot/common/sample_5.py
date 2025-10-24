def common(l1: list, l2: list):
    """Return a sorted list of unique elements common to both lists."""
    s2 = frozenset(l2)  # hashable, fast membership
    return sorted(set(filter(lambda x: x in s2, l1)))

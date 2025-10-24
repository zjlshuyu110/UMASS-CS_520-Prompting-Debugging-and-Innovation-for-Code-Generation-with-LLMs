def common(l1: list, l2: list):
    """Find common elements using set.intersection()."""
    if not l1 or not l2:
        return []
    return sorted(list(set(l1).intersection(set(l2))))
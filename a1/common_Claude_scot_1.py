def common(l1: list, l2: list):
    """Find common elements using set intersection."""
    return sorted(list(set(l1) & set(l2)))
def common(l1: list, l2: list):
    """Return a sorted list of unique elements common to both lists."""
    in_l2 = set(l2)
    hits = set()
    for x in l1:
        if x in in_l2:
            hits.add(x)
    return sorted(hits)

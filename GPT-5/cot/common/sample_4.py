def common(l1: list, l2: list):
    """Return a sorted list of unique elements common to both lists."""
    seen_in_l1 = {}
    for x in l1:
        seen_in_l1[x] = True
    hits = {}
    for y in l2:
        if y in seen_in_l1:
            hits[y] = True
    return sorted(hits.keys())

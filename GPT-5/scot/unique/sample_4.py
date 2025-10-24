def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    unique_items = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(unique_items)

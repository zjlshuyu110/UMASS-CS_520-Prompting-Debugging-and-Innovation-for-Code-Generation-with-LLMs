def unique(l: list):
    """Return sorted unique elements in a list."""
    return sorted(dict.fromkeys(l))

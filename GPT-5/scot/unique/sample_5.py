from functools import reduce

def unique(l: list):
    """Return sorted unique elements in a list."""
    result = reduce(lambda acc, x: acc if x in acc else acc + [x], l, [])
    return sorted(result)

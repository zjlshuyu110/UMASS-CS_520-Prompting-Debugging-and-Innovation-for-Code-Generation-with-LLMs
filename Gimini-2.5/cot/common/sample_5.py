def common(l1: list, l2: list) -> list:
    """
    Returns a sorted list of unique elements present in both input lists 
    in a condensed, single-line set intersection format.
    """
    return sorted(list(set(l1) & set(l2)))
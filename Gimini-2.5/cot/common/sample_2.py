def common(l1: list, l2: list) -> list:
    """
    Returns a sorted list of unique elements present in both input lists 
    using the set .intersection() method.
    """
    # Create sets and use the method for intersection.
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1.intersection(set2)
    return sorted(list(common_elements))
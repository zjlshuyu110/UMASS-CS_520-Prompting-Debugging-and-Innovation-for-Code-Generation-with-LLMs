def common(l1: list, l2: list) -> list:
    """
    Returns a sorted list of unique elements present in both input lists 
    by checking membership in a set via list comprehension.
    """
    # Convert the second list to a set for O(1) average time lookups.
    set_l2 = set(l2)
    
    # Use a list comprehension to find common elements. 
    # Use set(l1) to automatically handle uniqueness from the first list.
    common_elements = [item for item in set(l1) if item in set_l2]
    
    # The result is already unique (from set(l1)) but needs sorting.
    return sorted(common_elements)
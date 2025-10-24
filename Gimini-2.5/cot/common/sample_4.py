def common(l1: list, l2: list) -> list:
    """
    Returns a sorted list of unique elements present in both input lists 
    using an iterative check and building a result set.
    """
    # Convert one list to a set for fast membership checking.
    set_l2 = set(l2)
    
    # Use a set to store unique common elements as we find them.
    result_set = set()
    
    # Iterate over the first list's unique elements.
    for element in set(l1):
        if element in set_l2:
            result_set.add(element)
            
    # Convert the final set to a list and sort it.
    return sorted(list(result_set))
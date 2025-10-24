def unique(l: list) -> list:
    """
    Returns a sorted list of unique elements using list.sort() in-place.
    """
    # 1. Get unique elements into a new list
    unique_list = list(set(l))
    
    # 2. Sort the list in-place
    unique_list.sort()
    
    return unique_list
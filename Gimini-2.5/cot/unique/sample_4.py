def unique(l: list) -> list:
    """
    Returns a sorted list of unique elements by sorting first and then iterating.
    """
    if not l:
        return []

    # Sorts the list, O(N log N)
    sorted_l = sorted(l)
    
    # Deduplication loop
    result = [sorted_l[0]]
    for i in range(1, len(sorted_l)):
        # Only keep the element if it's different from the previous one
        if sorted_l[i] != sorted_l[i-1]:
            result.append(sorted_l[i])
            
    return result
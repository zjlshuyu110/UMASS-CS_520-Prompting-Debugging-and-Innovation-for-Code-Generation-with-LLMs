def unique(l: list) -> list:
    """
    Returns a sorted list of unique elements using a set for manual tracking.
    """
    seen = set()
    result = []
    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    # The list 'result' now contains unique elements in their first-appearance order.
    # We must now sort it as required.
    return sorted(result)
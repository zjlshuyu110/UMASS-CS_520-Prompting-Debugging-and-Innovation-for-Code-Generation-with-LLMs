def unique(l: list):
    """
    Use a set to track seen elements while maintaining uniqueness,
    then sort at the end.
    """
    seen = set()
    result = []
    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return sorted(result)
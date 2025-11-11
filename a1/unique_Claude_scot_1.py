def unique(l: list):
    """Return a sorted list of unique elements from the input list.
    
    Args:
        l: Input list that may contain duplicates
        
    Returns:
        A new sorted list containing only unique elements
        
    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
        >>> unique([])
        []
    """
    return sorted(set(l))
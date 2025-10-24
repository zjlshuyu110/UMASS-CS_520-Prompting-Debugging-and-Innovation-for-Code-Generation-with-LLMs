def unique(l: list) -> list:
    """
    Returns a sorted list of unique elements from the input list.
    
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # 1. Use set() for O(N) uniqueness check
    # 2. Use sorted() to get a new, sorted list from the set's elements
    return sorted(set(l))

# Example usage (for testing, not part of the required module)
# print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# print(unique([]))
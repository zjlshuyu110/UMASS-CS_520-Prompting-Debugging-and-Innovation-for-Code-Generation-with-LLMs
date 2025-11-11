def common(l1: list, l2: list) -> list:
    """
    Returns a sorted list of unique elements present in both input lists 
    using set intersection.
    """
    # Convert lists to sets, find the intersection, convert back to list, and sort.
    common_elements = set(l1) & set(l2)
    return sorted(list(common_elements))

# Example testing (as required by the reasoning, not the final output)
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])) # [1, 5, 653]
# print(common([5, 3, 2, 8], [3, 2])) # [2, 3]
# print(common([], [1, 2])) # []
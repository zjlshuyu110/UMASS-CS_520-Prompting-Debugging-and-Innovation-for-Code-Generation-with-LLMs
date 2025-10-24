"""
Implementation 1: Set Intersection Operator (Idiomatic Python)
Uses set conversion and the & operator for the most efficient intersection.
"""

from typing import List

def common(l1: List, l2: List) -> List:
    """
    Returns a sorted list of unique common elements found in both l1 and l2.

    Args:
        l1: The first list.
        l2: The second list.

    Returns:
        A sorted list of unique common elements.
    """
    # 1. Convert lists to sets to handle duplicates and enable fast intersection.
    set1 = set(l1)
    set2 = set(l2)

    # 2. Find the intersection of the two sets.
    common_elements_set = set1 & set2

    # 3. Convert the resulting set to a list and 4. sort it before returning.
    result = sorted(list(common_elements_set))
    
    return result

# Example behaviors (for verification):
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# print(common([5, 3, 2, 8], [3, 2]))
# print(common([], [1, 2]))
# print(common([10, 20], [30, 40]))

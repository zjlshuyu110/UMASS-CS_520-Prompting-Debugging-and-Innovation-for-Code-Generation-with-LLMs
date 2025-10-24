"""
Implementation 2: List Comprehension with Set Membership
Converts only one list (l1) to a set for fast lookup and uses a list 
comprehension over the unique elements of l2 to find matches.
"""

from typing import List

def common(l1: List, l2: List) -> List:
    """
    Returns a sorted list of unique common elements found in both l1 and l2.
    """
    # 1. Convert the first list to a set for fast O(1) membership checking.
    set1 = set(l1)

    # 2. Use a set of l2 to get unique elements from the second list, and then
    #    filter these unique elements using a list comprehension to check 
    #    if they exist in set1.
    common_elements = [item for item in set(l2) if item in set1]

    # 3. Sort the resulting list of common elements.
    return sorted(common_elements)

# Example behaviors (for verification):
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# print(common([5, 3, 2, 8], [3, 2]))
# print(common([], [1, 2]))

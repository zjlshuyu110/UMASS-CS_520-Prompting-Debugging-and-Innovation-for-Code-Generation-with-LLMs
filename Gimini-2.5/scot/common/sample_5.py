"""
Implementation 5: Utilizing set.intersection() Method
Explicitly uses the set.intersection() method, which is functionally 
identical to the & operator but slightly more verbose.
"""

from typing import List

def common(l1: List, l2: List) -> List:
    """
    Returns a sorted list of unique common elements found in both l1 and l2.
    """
    # 1. Convert lists to sets to handle duplicates.
    set1 = set(l1)
    set2 = set(l2)

    # 2. Find the intersection using the explicit method call.
    common_elements_set = set1.intersection(set2)

    # 3. Convert the resulting set to a list and 4. sort it before returning.
    result = sorted(list(common_elements_set))
    
    return result

# Example behaviors (for verification):
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# print(common([5, 3, 2, 8], [3, 2]))
# print(common([], [1, 2]))

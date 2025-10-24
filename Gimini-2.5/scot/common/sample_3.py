"""
Implementation 3: Manual Iteration and Collection
Uses two sets for input cleanup and then manually iterates through the 
smaller set, collecting matches in a third set for uniqueness guarantee.
"""

from typing import List

def common(l1: List, l2: List) -> List:
    """
    Returns a sorted list of unique common elements found in both l1 and l2.
    """
    # 1. Convert both lists to sets for uniqueness and fast lookup.
    set1 = set(l1)
    set2 = set(l2)
    
    # Optional optimization: iterate over the smaller set.
    if len(set1) > len(set2):
        smaller_set, larger_set = set2, set1
    else:
        smaller_set, larger_set = set1, set2

    # 2. Manually find common elements and store them in a result set.
    result_set = set()
    for item in smaller_set:
        if item in larger_set:
            # Add to the result set. Since it's a set, uniqueness is guaranteed.
            result_set.add(item)

    # 3. Convert the result set to a list and 4. sort it.
    return sorted(list(result_set))

# Example behaviors (for verification):
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# print(common([5, 3, 2, 8], [3, 2]))
# print(common([], [1, 2]))

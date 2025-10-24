"""
Implementation 4: Utilizing filter and lambda (Functional Style)
Uses the filter function with a lambda to check membership against a set, 
and relies on the first set conversion (set(l2)) to guarantee uniqueness 
of the elements being filtered.
"""

from typing import List

def common(l1: List, l2: List) -> List:
    """
    Returns a sorted list of unique common elements found in both l1 and l2.
    """
    # 1. Create a set from the first list for fast membership checks.
    set1 = set(l1)

    # 2. Get unique elements from l2 (using set(l2)) and filter them.
    #    The filter function keeps only items 'x' where the lambda returns True 
    #    (i.e., x is present in set1).
    common_iterator = filter(lambda x: x in set1, set(l2))

    # 3. Convert the iterator to a list and 4. sort it.
    return sorted(list(common_iterator))

# Example behaviors (for verification):
# print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# print(common([5, 3, 2, 8], [3, 2]))
# print(common([], [1, 2]))

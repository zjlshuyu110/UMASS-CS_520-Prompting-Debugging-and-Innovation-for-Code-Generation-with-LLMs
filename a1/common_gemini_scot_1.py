
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


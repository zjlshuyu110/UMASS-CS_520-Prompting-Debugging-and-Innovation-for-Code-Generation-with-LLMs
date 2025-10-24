import collections
# --- Implementation 1: Most Pythonic (Set and Sorted) ---
# This is the canonical, simplest, and most efficient approach for the task.
def unique(l: list) -> list:
    """
    Returns a new list containing sorted unique elements using the built-in set and sorted functions.
    (Most Pythonic and generally fastest).
    """
    # 1. De-duplicate using set
    unique_set = set(l)
    # 2. Convert to list and sort
    return sorted(list(unique_set))
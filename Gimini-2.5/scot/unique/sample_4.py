import collections
# --- Implementation 4: Using Dictionary Keys for Uniqueness and Manual Sort ---
# Demonstrates using a dictionary (hash map) to achieve uniqueness, similar to a set.
def unique(l: list) -> list:
    """
    Returns a new list containing sorted unique elements by leveraging dictionary keys
    for fast de-duplication, followed by a manual sort.
    """
    # 1. Use dict.fromkeys to quickly get unique keys (and preserve insertion order, though ignored here)
    unique_dict = dict.fromkeys(l)
    
    # 2. Get keys as a list
    result = list(unique_dict.keys())
    
    # 3. Sort the list (using the list's built-in sort method)
    result.sort()
    return result
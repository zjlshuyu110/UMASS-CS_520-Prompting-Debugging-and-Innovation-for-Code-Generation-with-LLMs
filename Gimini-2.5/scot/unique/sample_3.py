import collections
# --- Implementation 3: Manual Iteration with 'in' Check (Less Efficient for large lists) ---
# A classic, but O(N^2) approach if using only lists, which shows a manual way to de-duplicate.
def unique(l: list) -> list:
    """
    Returns a new list containing sorted unique elements by manually checking
    for existence in a result list, and then sorting the result.
    """
    unique_elements = []
    
    # 1. Iterate through the input list
    for item in l:
        # 2. Add element only if it hasn't been added yet (O(N) check per element)
        if item not in unique_elements:
            unique_elements.append(item)
            
    # 3. Sort the final unique list
    unique_elements.sort()
    return unique_elements
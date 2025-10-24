import collections
# --- Implementation 2: Sort First, then Sequential Check ---
# Avoids using a hash set, relying only on sorting and sequential comparison.
# This approach works well when element types are unhashable but sortable.
def unique(l: list) -> list:
    """
    Returns a new list containing sorted unique elements by sorting the list first,
    and then iterating to collect only non-duplicate adjacent elements.
    """
    if not l:
        return []

    # 1. Create a sorted copy (does not modify the original list l)
    sorted_l = sorted(l)
    
    result = []
    # 2. Iterate and append only if the current item is different from the last one added
    for item in sorted_l:
        if not result or item != result[-1]:
            result.append(item)
            
    return result
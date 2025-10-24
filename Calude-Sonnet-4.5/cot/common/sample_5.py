# Implementation 5: Manual iteration with explicit checks
def common(l1: list, l2: list):
    """Return sorted list of unique elements present in both lists."""
    seen = set()
    result = []
    set2 = set(l2)
    
    for item in l1:
        if item in set2 and item not in seen:
            result.append(item)
            seen.add(item)
    
    return sorted(result)
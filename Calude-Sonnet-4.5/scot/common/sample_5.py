def common(l1: list, l2: list):
    """Find common elements using two-pointer technique on sorted lists."""
    if not l1 or not l2:
        return []
    
    # Create sorted copies to avoid modifying originals
    sorted_l1 = sorted(set(l1))
    sorted_l2 = sorted(set(l2))
    
    result = []
    i, j = 0, 0
    
    while i < len(sorted_l1) and j < len(sorted_l2):
        if sorted_l1[i] == sorted_l2[j]:
            result.append(sorted_l1[i])
            i += 1
            j += 1
        elif sorted_l1[i] < sorted_l2[j]:
            i += 1
        else:
            j += 1
    
    return result
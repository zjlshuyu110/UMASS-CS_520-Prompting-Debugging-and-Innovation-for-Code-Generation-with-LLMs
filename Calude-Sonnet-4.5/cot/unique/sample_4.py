# Implementation 4: Sort first, then remove consecutive duplicates
def unique(l: list):
    """
    Sort the list first, then iterate through removing consecutive duplicates.
    This approach is useful when you want to avoid sets.
    """
    if not l:
        return []
    
    sorted_list = sorted(l)
    result = [sorted_list[0]]
    
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            result.append(sorted_list[i])
    
    return result
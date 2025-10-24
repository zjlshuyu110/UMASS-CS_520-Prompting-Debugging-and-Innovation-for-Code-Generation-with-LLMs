from typing import List, Any

def common(l1: list, l2: list):
    """
    Return a sorted list of unique elements present in both l1 and l2,
    using a two-pointer sweep on sorted copies and skipping duplicates.
    """
    a = sorted(l1)
    b = sorted(l2)
    i = j = 0
    result = []
    last_added = object()  # sentinel to avoid duplicates in output

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if a[i] is not last_added:
                result.append(a[i])
                last_added = a[i]
            # advance past duplicates in both lists
            val = a[i]
            while i < len(a) and a[i] == val:
                i += 1
            while j < len(b) and b[j] == val:
                j += 1
        elif a[i] < b[j]:
            val = a[i]
            while i < len(a) and a[i] == val:
                i += 1
        else:
            val = b[j]
            while j < len(b) and b[j] == val:
                j += 1

    return result

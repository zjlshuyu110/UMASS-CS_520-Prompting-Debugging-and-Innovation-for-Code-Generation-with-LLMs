from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold <= 0 or len(numbers) < 2:
        return False

    arr = sorted(x for x in numbers if not math.isnan(x))
    i = 0
    for j in range(1, len(arr)):
        # shrink left until diff < threshold or i reaches j
        while i < j and (arr[j] - arr[i] >= threshold) and (arr[j] != arr[i]):
            i += 1
        # if equal duplicates (incl. inf==inf), diff is 0 < threshold
        if arr[j] == arr[i] or arr[j] - arr[i] < threshold:
            return True
    return False

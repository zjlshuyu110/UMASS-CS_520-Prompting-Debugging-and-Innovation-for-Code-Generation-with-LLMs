from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold <= 0 or len(numbers) < 2:
        return False

    arr = sorted(x for x in numbers if not math.isnan(x))
    n = len(arr)
    for i in range(n):
        # If duplicates, immediate success (incl. inf==inf)
        if i + 1 < n and arr[i] == arr[i+1]:
            return True
        for j in range(i + 1, n):
            if math.isinf(arr[i]) and math.isinf(arr[j]):
                return True  # same sign inf handled by equality above; keep for clarity
            diff = arr[j] - arr[i]
            if diff < threshold:
                return True
            # Since sorted, further j will only increase diff
            break
    return False

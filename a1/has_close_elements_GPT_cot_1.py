from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if any two numbers in the list are closer than the given threshold.
    Returns True iff there exist i != j such that |numbers[i] - numbers[j]| < threshold.
    """
    if threshold <= 0 or len(numbers) < 2:
        return False

    arr = sorted(numbers)
    prev = None

    for x in arr:
        if math.isnan(x):
            prev = None  # don't compare across NaNs
            continue
        if prev is not None:
            # Handle exact equality (incl. inf==inf) without doing inf - inf
            if x == prev:
                return True  # difference is 0 < threshold since threshold > 0
            diff = abs(x - prev)
            if diff < threshold:
                return True
        prev = x

    return False

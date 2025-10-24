from typing import List
import bisect

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Insert each number into a sorted list (via bisect) and check neighbors.
    Raises ValueError if 'numbers' is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    if threshold <= 0:
        return False

    seen: List[float] = []
    for x in numbers:
        pos = bisect.bisect_left(seen, x)
        if pos > 0 and x - seen[pos - 1] < threshold:
            return True
        if pos < len(seen) and seen[pos] - x < threshold:
            return True
        seen.insert(pos, x)
    return False

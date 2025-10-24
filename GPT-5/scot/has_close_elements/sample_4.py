from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Bucket-based check: width = threshold.
    Only same or adjacent buckets can host a pair within 'threshold'.
    Raises ValueError if 'numbers' is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    if threshold <= 0:
        return False

    buckets: dict[int, float] = {}
    w = threshold  # bucket width

    for x in numbers:
        b = math.floor(x / w)
        # Check same bucket
        if b in buckets and abs(x - buckets[b]) < threshold:
            return True
        # Check adjacent buckets
        if (b - 1) in buckets and abs(x - buckets[b - 1]) < threshold:
            return True
        if (b + 1) in buckets and abs(x - buckets[b + 1]) < threshold:
            return True
        # Store representative (any value is fine; we only need existence)
        buckets[b] = x

    return False

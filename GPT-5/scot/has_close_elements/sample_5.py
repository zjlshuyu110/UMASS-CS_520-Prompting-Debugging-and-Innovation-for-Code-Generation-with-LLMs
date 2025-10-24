from typing import List
import heapq

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Heapify and pop in ascending order; check differences of consecutive pops.
    Raises ValueError if 'numbers' is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    if threshold <= 0:
        return False

    heap = list(numbers)
    heapq.heapify(heap)

    prev = heapq.heappop(heap)
    while heap:
        cur = heapq.heappop(heap)
        if cur - prev < threshold:
            return True
        prev = cur
    return False

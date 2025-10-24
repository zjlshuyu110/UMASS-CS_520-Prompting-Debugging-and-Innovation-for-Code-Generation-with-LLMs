from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Uses itertools.combinations and any() for a concise check (O(N^2))."""
    
    # Check if any pair (a, b) from combinations satisfies the condition
    return any(
        abs(a - b) < threshold
        for a, b in combinations(numbers, 2)
    )
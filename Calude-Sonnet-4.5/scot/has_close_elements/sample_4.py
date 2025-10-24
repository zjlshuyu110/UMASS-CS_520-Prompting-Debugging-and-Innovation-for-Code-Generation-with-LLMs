from typing import List
from itertools import combinations

# Implementation 4: Using itertools.combinations (Functional Style)
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check using itertools.combinations for clean pair generation."""
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return any(
        abs(a - b) < threshold
        for a, b in combinations(numbers, 2)
    )

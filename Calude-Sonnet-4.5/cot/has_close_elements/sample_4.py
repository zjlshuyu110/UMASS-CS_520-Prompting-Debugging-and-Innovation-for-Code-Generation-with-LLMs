from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Functional approach using any() with generator expression."""
    sorted_numbers = sorted(numbers)
    
    return any(
        abs(sorted_numbers[i + 1] - sorted_numbers[i]) < threshold
        for i in range(len(sorted_numbers) - 1)
    )
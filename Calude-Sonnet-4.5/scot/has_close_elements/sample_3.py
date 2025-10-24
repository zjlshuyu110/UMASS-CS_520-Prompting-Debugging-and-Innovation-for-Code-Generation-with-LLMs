from typing import List
from itertools import combinations

# Implementation 3: Pythonic with Enumerate and Generator Expression
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check using enumerate and any() with generator for lazy evaluation."""
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return any(
        abs(numbers[i] - numbers[j]) < threshold
        for i in range(len(numbers))
        for j in range(i + 1, len(numbers))
    )

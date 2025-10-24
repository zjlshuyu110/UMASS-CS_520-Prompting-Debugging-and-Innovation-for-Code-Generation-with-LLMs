from typing import List
from itertools import combinations

# Implementation 1: Classic Brute Force with Nested Loops
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers are closer than threshold using nested loops."""
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
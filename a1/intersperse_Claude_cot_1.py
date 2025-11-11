from typing import List


# Implementation 1: Simple iterative with enumerate
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Iterative approach checking index position."""
    if len(numbers) <= 1:
        return numbers[:]  # Return a copy
    
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Not the last element
            result.append(delimeter)
    return result
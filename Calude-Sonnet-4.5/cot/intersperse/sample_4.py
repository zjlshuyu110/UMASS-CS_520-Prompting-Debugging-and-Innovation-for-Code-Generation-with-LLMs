from typing import List

# Implementation 4: Recursive approach
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Recursively build the interspersed list."""
    if len(numbers) <= 1:
        return numbers[:]
    
    if len(numbers) == 2:
        return [numbers[0], delimeter, numbers[1]]
    
    return [numbers[0], delimeter] + intersperse(numbers[1:], delimeter)
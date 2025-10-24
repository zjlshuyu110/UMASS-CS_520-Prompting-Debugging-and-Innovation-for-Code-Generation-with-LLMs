from typing import List
# Implementation 2: Using extend with slicing
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Build result by extending pairs for all but last element."""
    if len(numbers) <= 1:
        return numbers[:]
    
    result = []
    for i in range(len(numbers) - 1):
        result.extend([numbers[i], delimeter])
    result.append(numbers[-1])
    return result
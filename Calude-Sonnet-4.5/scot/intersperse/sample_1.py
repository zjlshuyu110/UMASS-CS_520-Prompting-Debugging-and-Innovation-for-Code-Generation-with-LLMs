from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert delimiter between consecutive elements using index-based iteration."""
    if len(numbers) <= 1:
        return numbers.copy()
    
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    
    return result
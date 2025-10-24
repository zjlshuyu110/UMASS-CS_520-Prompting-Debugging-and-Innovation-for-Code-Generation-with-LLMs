from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert delimiter using extend method for efficient building."""
    if len(numbers) <= 1:
        return numbers.copy()
    
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimeter)
        result.append(num)
    
    return result
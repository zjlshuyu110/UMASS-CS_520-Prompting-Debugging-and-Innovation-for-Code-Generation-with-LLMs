from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert delimiter using list comprehension and enumerate."""
    if len(numbers) <= 1:
        return numbers.copy()
    
    result = [elem for i, num in enumerate(numbers[:-1]) 
              for elem in (num, delimeter)]
    result.append(numbers[-1])
    
    return result
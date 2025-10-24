from typing import List, Callable

# Helper for the examples below
DELIMITER = 99

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts the delimeter using a nested list comprehension to create
    a sequence of [element, delimeter] pairs, flattening the result.
    """
    if not numbers:
        return []
        
    # The inner comprehension creates lists like: [[1, 4], [2, 4], [3]]
    # The outer comprehension flattens that structure.
    return [
        item 
        for i in range(len(numbers)) 
        for item in (
            [numbers[i], delimeter] 
            if i < len(numbers) - 1 
            else [numbers[i]]
        )
    ]
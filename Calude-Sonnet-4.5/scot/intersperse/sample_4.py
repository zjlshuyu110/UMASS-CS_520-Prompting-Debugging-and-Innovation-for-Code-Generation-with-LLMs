from typing import List
from itertools import chain

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert delimiter using itertools.chain for functional style."""
    if len(numbers) <= 1:
        return numbers.copy()
    
    # Create pairs of (element, delimiter) for all but the last element
    pairs = [[num, delimeter] for num in numbers[:-1]]
    # Flatten the pairs and add the last element
    result = list(chain.from_iterable(pairs)) + [numbers[-1]]
    
    return result
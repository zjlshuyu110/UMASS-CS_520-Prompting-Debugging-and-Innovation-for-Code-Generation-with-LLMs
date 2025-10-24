from typing import List
from itertools import repeat

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Uses zip to pair elements with delimiters and list() flattening."""
    
    n = len(numbers)
    if n < 2:
        return list(numbers)
    
    # We need n-1 delimiters.
    delimiters = list(repeat(delimeter, n - 1))
    
    # We are zipping [d, d, ...] with [2, 3, ...]
    # The first element [1] is prepended manually.
    
    # Pairs: (d, 2), (d, 3)
    pairs = zip(delimiters, numbers[1:])
    
    # Flatten the result: [[d, 2], [d, 3]] -> [d, 2, d, 3]
    # Use chain.from_iterable for robust flattening, or a comprehension
    
    # Manual flattening:
    interspersed_elements = []
    for d, num in pairs:
        interspersed_elements.append(d)
        interspersed_elements.append(num)
        
    # Prepend the first element
    return [numbers[0]] + interspersed_elements
from typing import List
from itertools import chain

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Uses itertools.chain.from_iterable to flatten the sequence of [delimiter, element] pairs."""
    if len(numbers) < 2:
        return list(numbers)
        
    # Generates: (num1), (delimiter, num2), (delimiter, num3), ...
    # The first element is treated separately for the chain.
    sequence = chain(
        (numbers[0],), 
        chain.from_iterable(
            (delimeter, num) for num in numbers[1:]
        )
    )
    
    return list(sequence)
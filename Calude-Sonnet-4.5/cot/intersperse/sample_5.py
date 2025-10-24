from typing import List

# Implementation 5: Using itertools.chain
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Use itertools.chain to flatten pairs."""
    from itertools import chain
    
    if len(numbers) <= 1:
        return numbers[:]
    
    # Create pairs of [num, delimeter] for all but the last element
    pairs = ([num, delimeter] for num in numbers[:-1])
    return list(chain.from_iterable(pairs)) + [numbers[-1]]
from typing import List
import itertools

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    # Chain all pairs and skip the trailing delimiter
    return list(itertools.chain.from_iterable(zip(numbers, [delimeter] * len(numbers))))[:-1]

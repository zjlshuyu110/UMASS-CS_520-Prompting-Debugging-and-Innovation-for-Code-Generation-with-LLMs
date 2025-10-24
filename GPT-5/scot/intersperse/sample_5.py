from typing import List
from functools import reduce

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    return reduce(lambda acc, x: acc + [delimeter, x], numbers[1:], [numbers[0]])

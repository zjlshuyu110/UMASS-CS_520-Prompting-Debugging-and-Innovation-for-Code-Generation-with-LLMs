from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    return sum(([n, delimeter] for n in numbers[:-1]), []) + [numbers[-1]]

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    pairs = [[n, delimeter] for n in numbers[:-1]]
    return sum(pairs, []) + [numbers[-1]]

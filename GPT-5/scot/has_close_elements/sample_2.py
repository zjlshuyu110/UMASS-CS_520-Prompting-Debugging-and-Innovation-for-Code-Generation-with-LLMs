from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Quadratic check over all pairs with early exit.
    Raises ValueError if 'numbers' is empty.
    """
    n = len(numbers)
    if n == 0:
        raise ValueError("numbers must not be empty")
    if threshold <= 0:
        return False

    for i in range(n - 1):
        ai = numbers[i]
        for j in range(i + 1, n):
            if abs(ai - numbers[j]) < threshold:
                return True
    return False

from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Return True if any two numbers are closer than 'threshold'; else False.
    Raises ValueError if 'numbers' is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    if threshold <= 0:
        return False

    arr = sorted(numbers)
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < threshold:
            return True
    return False

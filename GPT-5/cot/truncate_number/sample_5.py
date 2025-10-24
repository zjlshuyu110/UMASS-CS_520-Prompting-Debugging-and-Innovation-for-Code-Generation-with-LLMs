from typing import *

def truncate_number(number: float) -> float:
    """Return the fractional part of a non-negative float."""
    # For non-negative numbers, int(number) is the floor.
    return number - int(number)

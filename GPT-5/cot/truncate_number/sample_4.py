from typing import *

def truncate_number(number: float) -> float:
    """Return the fractional part of a non-negative float."""
    # divmod returns (quotient, remainder); for non-negative numbers,
    # remainder is in [0.0, 1.0).
    _, rem = divmod(number, 1.0)
    return rem

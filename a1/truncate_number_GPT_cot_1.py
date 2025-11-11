from math import modf
from typing import *

def truncate_number(number: float) -> float:
    """Return the fractional part of a non-negative float."""
    frac, _ = modf(number)
    return frac

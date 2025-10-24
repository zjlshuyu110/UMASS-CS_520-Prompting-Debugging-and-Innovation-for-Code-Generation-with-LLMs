from math import floor
from typing import *

def truncate_number(number: float) -> float:
    """Return the fractional part of a non-negative float."""
    return number - floor(number)

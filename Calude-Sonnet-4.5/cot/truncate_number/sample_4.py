import math

def truncate_number(number: float) -> float:
    """Return the decimal part using modf (returns fractional, integer)."""
    return math.modf(number)[0]
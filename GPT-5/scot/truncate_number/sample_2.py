import math

def truncate_number(number: float) -> float:
    """Return the fractional part using floor subtraction."""
    return round(number - math.floor(number), 10)

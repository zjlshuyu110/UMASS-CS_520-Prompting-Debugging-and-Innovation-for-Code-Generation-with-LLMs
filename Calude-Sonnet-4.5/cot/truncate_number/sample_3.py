import math

def truncate_number(number: float) -> float:
    """Return the decimal part using floor function."""
    return number - math.floor(number)

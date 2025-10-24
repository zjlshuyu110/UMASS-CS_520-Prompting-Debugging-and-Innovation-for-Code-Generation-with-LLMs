import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal (fractional) part of a non-negative float
    by subtracting the integer part obtained via int().
    """
    integer_part = int(number)
    return number - integer_part
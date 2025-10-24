import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal (fractional) part of a non-negative float
    by subtracting the floor of the number.
    """
    integer_part = math.floor(number)
    return number - integer_part
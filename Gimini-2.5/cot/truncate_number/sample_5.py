import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal (fractional) part of a non-negative float
    by subtracting the truncated integer part.
    """
    integer_part = math.trunc(number)
    return number - integer_part
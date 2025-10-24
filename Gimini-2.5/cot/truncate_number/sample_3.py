import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal (fractional) part of a non-negative float
    by using math.modf().
    """
    # math.modf returns a tuple (fractional_part, integer_part)
    fractional_part, _ = math.modf(number)
    return fractional_part
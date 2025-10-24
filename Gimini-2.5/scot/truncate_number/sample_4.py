import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive float using the dedicated math.modf function.
    (D, I) = modf(N).
    """
    decimal_part, _ = math.modf(number)
    return decimal_part
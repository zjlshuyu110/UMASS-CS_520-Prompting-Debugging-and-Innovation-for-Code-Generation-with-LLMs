import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive float using math.floor().
    D = N - floor(N).
    """
    integer_part = math.floor(number)
    decimal_part = number - integer_part
    return decimal_part
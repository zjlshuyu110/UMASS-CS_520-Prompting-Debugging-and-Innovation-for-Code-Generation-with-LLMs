import math

def truncate_number(number: float) -> float:
    """
    Returns the decimal (fractional) part of a non-negative float
    using the float modulo operator (%).
    """
    return number % 1.0
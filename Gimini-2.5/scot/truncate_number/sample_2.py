import math
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive float using the modulo operator (%).
    D = N % 1.
    """
    # N % 1 is equivalent to N - floor(N) for positive numbers.
    decimal_part = number % 1.0
    
    # A small adjustment for cases where the result is extremely close to 1 due to
    # floating point error (e.g., 2.999... % 1 might be 0.999...).
    # Though often unnecessary, it adds robustness.
    if math.isclose(decimal_part, 1.0):
        return 0.0
    
    return decimal_part
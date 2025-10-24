def truncate_number(number: float) -> float:
    """
    Return the decimal part using modulo 1.
    The remainder when dividing by 1 is the fractional part.
    """
    return number % 1
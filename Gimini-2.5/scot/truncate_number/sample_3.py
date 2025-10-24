def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive float by casting to int().
    """
    # For positive numbers, int(N) is equivalent to floor(N).
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
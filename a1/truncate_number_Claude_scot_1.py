def truncate_number(number: float) -> float:
    """
    Return the decimal part by subtracting the integer part.
    Uses int() to extract the integer portion.
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
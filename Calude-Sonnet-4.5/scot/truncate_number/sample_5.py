def truncate_number(number: float) -> float:
    """
    Return the decimal part using floor division.
    number // 1 gives the integer part as a float.
    """
    integer_part = number // 1
    return number - integer_part
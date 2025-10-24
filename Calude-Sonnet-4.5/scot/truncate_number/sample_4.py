def truncate_number(number: float) -> float:
    """
    Return the decimal part using math.modf().
    modf() returns (fractional_part, integer_part) as a tuple.
    """
    import math
    fractional_part, integer_part = math.modf(number)
    return fractional_part
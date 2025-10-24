def truncate_number(number: float) -> float:
    """
    Return the decimal part using math.floor().
    Floor gives the largest integer not greater than number.
    """
    import math
    return number - math.floor(number)

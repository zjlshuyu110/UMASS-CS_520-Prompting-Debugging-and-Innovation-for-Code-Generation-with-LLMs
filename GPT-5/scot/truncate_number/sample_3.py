import math

def truncate_number(number: float) -> float:
    """Return fractional part using math.modf (splits into frac, int)."""
    frac, _ = math.modf(number)
    return round(frac, 10)

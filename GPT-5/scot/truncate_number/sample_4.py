def truncate_number(number: float) -> float:
    """Return fractional part using divmod with 1."""
    _, frac = divmod(number, 1)
    return round(frac, 10)

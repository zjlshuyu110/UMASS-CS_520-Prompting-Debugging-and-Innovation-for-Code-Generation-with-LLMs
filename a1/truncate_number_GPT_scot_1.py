def truncate_number(number: float) -> float:
    """Return the fractional part of a non-negative float."""
    return round(number - int(number), 10)

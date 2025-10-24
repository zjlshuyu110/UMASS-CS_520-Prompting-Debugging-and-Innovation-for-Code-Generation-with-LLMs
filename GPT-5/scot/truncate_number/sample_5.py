def truncate_number(number: float) -> float:
    """Return fractional part by parsing string representation."""
    s = f"{number:.15f}"
    if "." not in s:
        return 0.0
    int_part, dec_part = s.split(".")
    return float("0." + dec_part.rstrip("0")) if dec_part.strip("0") else 0.0

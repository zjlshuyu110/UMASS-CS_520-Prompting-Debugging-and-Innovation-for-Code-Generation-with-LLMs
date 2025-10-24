def multiply(a, b):
    """Return the product of the unit digits of two integers."""
    # divmod returns (quotient, remainder)
    # We only need the remainder (unit digit)
    _, unit_a = divmod(abs(a), 10)
    _, unit_b = divmod(abs(b), 10)
    return unit_a * unit_b
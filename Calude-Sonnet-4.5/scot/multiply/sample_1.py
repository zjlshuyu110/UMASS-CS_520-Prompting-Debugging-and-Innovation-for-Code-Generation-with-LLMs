def multiply(a, b):
    """Return the product of the unit digits of two integers."""
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10
    return unit_a * unit_b
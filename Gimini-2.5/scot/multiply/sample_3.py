def multiply(a, b):
    """
    Returns the product of the unit digits of a and b.
    Uses a concise ternary operator for absolute value simulation before modulo.
    """
    # Extract unit digit: (a if a >= 0 else -a) % 10 is equivalent to abs(a) % 10
    unit_a = (a if a >= 0 else -a) % 10
    unit_b = (b if b >= 0 else -b) % 10

    return unit_a * unit_b
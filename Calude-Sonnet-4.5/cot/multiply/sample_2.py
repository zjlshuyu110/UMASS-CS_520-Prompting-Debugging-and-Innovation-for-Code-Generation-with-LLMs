def multiply(a, b):
    """Return the product of the unit digits of a and b."""
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    return unit_digit_a * unit_digit_b
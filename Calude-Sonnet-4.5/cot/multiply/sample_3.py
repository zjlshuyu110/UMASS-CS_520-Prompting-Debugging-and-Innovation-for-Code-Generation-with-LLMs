def multiply(a, b):
    """Return the product of the unit digits of a and b."""
    unit_digit_a = int(str(abs(a))[-1])
    unit_digit_b = int(str(abs(b))[-1])
    return unit_digit_a * unit_digit_b
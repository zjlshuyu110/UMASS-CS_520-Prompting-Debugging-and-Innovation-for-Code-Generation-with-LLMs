def multiply(a, b):
    """Return the product of the unit digits of two integers."""
    last_digit_a = int(str(abs(a))[-1])
    last_digit_b = int(str(abs(b))[-1])
    return last_digit_a * last_digit_b
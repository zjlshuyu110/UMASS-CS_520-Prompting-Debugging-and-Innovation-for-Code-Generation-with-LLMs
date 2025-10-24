def multiply(a, b):
    """
    Returns the product of the unit digits of a and b.
    Uses abs() and the modulo operator (%).
    """
    # 1. Get Absolute Values and 2/3. Extract Unit Digits
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10

    # 4. Calculate Product
    return unit_a * unit_b
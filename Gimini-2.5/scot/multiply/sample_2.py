def multiply(a, b):
    """
    Returns the product of the unit digits of a and b.
    Handles negative numbers using explicit conditional checks.
    """
    # Handle absolute value calculation manually
    a_abs = a if a >= 0 else -a
    b_abs = b if b >= 0 else -b

    # Extract Unit Digits
    unit_a = a_abs % 10
    unit_b = b_abs % 10

    # Calculate Product
    return unit_a * unit_b
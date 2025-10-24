def multiply(a, b):
    """
    Returns the product of the unit digits of a and b (using absolute values).
    """
    # Get the unit digit of 'a' using absolute value and modulo 10
    unit_a = abs(a) % 10
    
    # Get the unit digit of 'b' using absolute value and modulo 10
    unit_b = abs(b) % 10
    
    return unit_a * unit_b
def multiply(a, b):
    """
    Returns the product of the unit digits of a and b, using string conversion.
    """
    # Convert absolute value of 'a' to string, take the last character, convert to int
    unit_a = int(str(abs(a))[-1])
    
    # Convert absolute value of 'b' to string, take the last character, convert to int
    unit_b = int(str(abs(b))[-1])
    
    return unit_a * unit_b
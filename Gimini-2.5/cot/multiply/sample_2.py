def multiply(a, b):
    """
    Returns the product of the unit digits of a and b (using absolute values).
    Uses a local lambda function for conciseness.
    """
    # Helper lambda to find the unit digit of a number
    get_unit_digit = lambda n: abs(n) % 10
    
    return get_unit_digit(a) * get_unit_digit(b)
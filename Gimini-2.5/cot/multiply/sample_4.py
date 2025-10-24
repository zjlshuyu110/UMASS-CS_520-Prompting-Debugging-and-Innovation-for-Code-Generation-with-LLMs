def multiply(a, b):
    """
    Returns the product of the unit digits of a and b, explicitly separating 
    absolute value calculation.
    """
    # 1. Get absolute values
    abs_a = abs(a)
    abs_b = abs(b)
    
    # 2. Get unit digits
    unit_a = abs_a % 10
    unit_b = abs_b % 10
    
    # 3. Return product
    return unit_a * unit_b
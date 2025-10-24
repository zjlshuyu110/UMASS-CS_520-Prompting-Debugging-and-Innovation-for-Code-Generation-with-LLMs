def multiply(a, b):
    """
    Returns the product of the unit digits of a and b.
    Uses an internal variable assignment to define the unit extraction logic once.
    """
    # Define the unit extraction logic
    get_unit_digit = lambda n: abs(n) % 10
    
    # 2/3. Extract Unit Digits
    unit_a = get_unit_digit(a)
    unit_b = get_unit_digit(b)

    # 4. Calculate Product
    return unit_a * unit_b
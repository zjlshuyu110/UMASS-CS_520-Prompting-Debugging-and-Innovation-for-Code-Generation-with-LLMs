def multiply(a, b):
    """Return the product of the unit digits of two integers."""
    # Convert to absolute values to handle negative numbers
    abs_a = abs(a)
    abs_b = abs(b)
    
    # Extract unit digits using modulo operation
    unit_digit_a = abs_a % 10
    unit_digit_b = abs_b % 10
    
    # Calculate and return the product
    product = unit_digit_a * unit_digit_b
    return product
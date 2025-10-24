def multiply(a, b):
    """
    Returns the product of the unit digits of a and b in a single expression.
    """
    return (abs(a) % 10) * (abs(b) % 10)
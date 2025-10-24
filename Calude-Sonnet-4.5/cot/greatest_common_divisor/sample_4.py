def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor using subtraction-based algorithm."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def greatest_common_divisor(a: int, b: int) -> int:
    """Subtraction-based Euclid; handles zeros and negatives."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

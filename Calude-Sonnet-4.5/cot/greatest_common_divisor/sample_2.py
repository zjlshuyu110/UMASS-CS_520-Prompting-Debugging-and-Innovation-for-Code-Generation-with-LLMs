def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using recursive Euclidean algorithm."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
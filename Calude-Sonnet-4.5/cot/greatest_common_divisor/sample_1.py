def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using iterative Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
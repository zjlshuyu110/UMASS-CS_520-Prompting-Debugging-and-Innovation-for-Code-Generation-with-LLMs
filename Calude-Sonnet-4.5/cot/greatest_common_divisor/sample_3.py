def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b with explicit ordering."""
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
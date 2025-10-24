def greatest_common_divisor(a: int, b: int) -> int:
    """Euclid with ordering and break-based loop style."""
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return a or b  # returns the non-zero one, or 0 if both zero
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

def greatest_common_divisor(a: int, b: int) -> int:
    """Stein's binary GCD: uses shifts and subtraction/mod-2 logic."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    # k = common power of two
    shift = (a | b) & -(a | b)  # lowest set bit of (a|b)
    k = 0
    while shift & 1 == 0:
        shift >>= 1
        k += 1

    # remove all factors of 2 from a
    while (a & 1) == 0:
        a >>= 1
    # loop
    while b != 0:
        # remove all factors of 2 from b
        while (b & 1) == 0:
            b >>= 1
        # ensure a <= b
        if a > b:
            a, b = b, a
        b -= a
    # restore common power of two
    return a << k

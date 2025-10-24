# --- Implementation 4: Naive Brute-Force Search (Factorization) ---
# Inefficient for large numbers, but simple to understand and a distinct approach.
def greatest_common_divisor(a: int, b: int) -> int:
    """Computes GCD by iterating downwards from the minimum of the two numbers."""
    u, v = abs(a), abs(b)

    # Handle special case GCD(0, 0) = 0, GCD(x, 0) = |x|
    if u == 0 and v == 0:
        return 0
    if u == 0:
        return v
    if v == 0:
        return u

    # The GCD must be less than or equal to the minimum of the two positive numbers.
    limit = min(u, v)
    
    # Iterate from the potential highest divisor down to 1.
    for i in range(limit, 0, -1):
        if (u % i == 0) and (v % i == 0):
            return i
            
    # Should be unreachable if initial checks passed and a, b are integers.
    return 1 # Fallback, GCD of any two positive numbers is at least 1.
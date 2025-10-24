def multiply(a, b):
    def unit_digit(n):
        return abs(n) % 10
    return unit_digit(a) * unit_digit(b)

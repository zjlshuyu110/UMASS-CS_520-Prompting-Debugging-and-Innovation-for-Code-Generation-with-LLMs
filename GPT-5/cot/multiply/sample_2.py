def multiply(a, b):
    _, ua = divmod(abs(a), 10)
    _, ub = divmod(abs(b), 10)
    return ua * ub

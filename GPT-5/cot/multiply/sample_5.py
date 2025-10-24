from operator import mod

def multiply(a, b):
    ua = mod(abs(a), 10)
    ub = mod(abs(b), 10)
    return ua * ub

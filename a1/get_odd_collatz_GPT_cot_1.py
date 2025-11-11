def get_odd_collatz(n):
    s = set()
    x = n
    while x != 1:
        if x % 2 == 1:
            s.add(x)
            x = 3 * x + 1
        else:
            x //= 2
    s.add(1)
    return sorted(s)

def get_odd_collatz(n):
    s = set()
    x = n
    while True:
        if x & 1:
            s.add(x)
            if x == 1:
                return sorted(s)
            x = 3 * x + 1
        else:
            x //= 2

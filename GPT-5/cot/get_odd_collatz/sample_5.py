def get_odd_collatz(n):
    s = set()
    x = n
    while True:
        while x % 2 == 0:
            x //= 2
        s.add(x)
        if x == 1:
            return sorted(s)
        x = 3 * x + 1

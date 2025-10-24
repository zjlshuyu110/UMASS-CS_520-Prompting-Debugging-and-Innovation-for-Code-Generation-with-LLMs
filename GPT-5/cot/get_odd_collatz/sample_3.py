def get_odd_collatz(n):
    s = set()
    x = n
    while True:
        if x % 2:
            s.add(x)
        if x == 1:
            return sorted(s)
        x = 3 * x + 1 if x % 2 else x // 2

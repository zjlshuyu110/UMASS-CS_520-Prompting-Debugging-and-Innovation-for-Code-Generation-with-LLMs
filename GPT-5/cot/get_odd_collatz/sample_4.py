def get_odd_collatz(n):
    seq = []
    x = n
    while True:
        seq.append(x)
        if x == 1:
            break
        x = 3 * x + 1 if x % 2 else x // 2
    return sorted({v for v in seq if v % 2})

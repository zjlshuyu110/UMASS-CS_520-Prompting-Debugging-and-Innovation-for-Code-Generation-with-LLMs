def get_odd_collatz(n):
    odds = set()
    while True:
        if n % 2:
            odds.add(n)
        if n == 1:
            break
        n = (3 * n + 1) if n % 2 else (n // 2)
    return sorted(odds)

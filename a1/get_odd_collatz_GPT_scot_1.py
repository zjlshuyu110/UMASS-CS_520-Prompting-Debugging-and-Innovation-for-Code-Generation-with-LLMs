def get_odd_collatz(n):
    odds = set()
    while n != 1:
        if n % 2 == 1:
            odds.add(n)
        n = 3 * n + 1 if n % 2 else n // 2
    odds.add(1)
    return sorted(odds)

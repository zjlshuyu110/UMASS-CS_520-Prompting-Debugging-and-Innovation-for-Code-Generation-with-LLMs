def get_odd_collatz(n):
    odds = set()

    def helper(x):
        odds.add(x) if x % 2 else None
        if x == 1:
            return
        helper(3 * x + 1 if x % 2 else x // 2)

    helper(n)
    return sorted(odds)

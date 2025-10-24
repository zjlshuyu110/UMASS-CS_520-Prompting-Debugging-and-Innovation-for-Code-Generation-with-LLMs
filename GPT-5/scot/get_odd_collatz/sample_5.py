def get_odd_collatz(n):
    def collatz_gen(x):
        while True:
            yield x
            if x == 1:
                break
            x = 3 * x + 1 if x % 2 else x // 2

    return sorted({num for num in collatz_gen(n) if num % 2})

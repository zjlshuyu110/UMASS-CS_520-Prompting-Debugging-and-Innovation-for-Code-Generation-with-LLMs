def get_odd_collatz(n):
    """Use a generator to yield odd numbers, collect in set."""
    def collatz_sequence(num):
        while num != 1:
            yield num
            num = num // 2 if num % 2 == 0 else 3 * n + 1
        yield 1
    
    odd_numbers = {num for num in collatz_sequence(n) if num % 2 == 1}
    return sorted(odd_numbers)
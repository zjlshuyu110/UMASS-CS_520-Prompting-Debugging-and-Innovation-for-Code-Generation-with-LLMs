def get_odd_collatz(n):
    sequence = []
    
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    
    sequence.append(1)
    
    odd_numbers = set(num for num in sequence if num % 2 == 1)
    return sorted(odd_numbers)
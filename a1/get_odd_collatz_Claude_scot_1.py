def get_odd_collatz(n):
    odd_numbers = set()
    current = n
    
    while current != 1:
        if current % 2 == 1:
            odd_numbers.add(current)
        
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    odd_numbers.add(1)
    return sorted(odd_numbers)
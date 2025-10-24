def get_odd_collatz(n):
    odd_numbers = []
    
    while n != 1:
        if n & 1:  # bitwise check for odd
            odd_numbers.append(n)
        
        if n & 1:
            n = 3 * n + 1
        else:
            n = n >> 1  # bitwise right shift for division by 2
    
    odd_numbers.append(1)
    return sorted(set(odd_numbers))
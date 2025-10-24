def get_odd_collatz(n):
    def collatz_helper(num, odds):
        if num == 1:
            odds.add(1)
            return
        
        if num % 2 == 1:
            odds.add(num)
        
        next_num = num // 2 if num % 2 == 0 else 3 * num + 1
        collatz_helper(next_num, odds)
    
    odd_set = set()
    collatz_helper(n, odd_set)
    return sorted(odd_set)
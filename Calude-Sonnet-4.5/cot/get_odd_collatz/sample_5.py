def get_odd_collatz(n):
    """Recursively collect odd numbers in the Collatz sequence."""
    def collatz_odds(num, odds):
        if num % 2 == 1:
            odds.add(num)
        
        if num == 1:
            return odds
        
        next_num = num // 2 if num % 2 == 0 else 3 * num + 1
        return collatz_odds(next_num, odds)
    
    return sorted(collatz_odds(n, set()))
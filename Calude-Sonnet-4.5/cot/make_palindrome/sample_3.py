def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    for i, _ in enumerate(string + ' '):  # +' ' to include len(string)
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    
    return string
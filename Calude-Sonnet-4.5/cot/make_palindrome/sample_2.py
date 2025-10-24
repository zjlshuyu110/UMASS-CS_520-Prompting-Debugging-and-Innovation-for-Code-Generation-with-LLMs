def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    i = 0
    while i <= len(string):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
        i += 1
    
    return string
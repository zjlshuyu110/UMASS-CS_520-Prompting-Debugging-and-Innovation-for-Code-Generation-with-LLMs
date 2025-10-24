def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Find first i where string[i:] is palindrome, then append reverse of string[:i]
    i = next((i for i in range(len(string) + 1) if is_palindrome(string[i:])), 0)
    return string + string[:i][::-1]
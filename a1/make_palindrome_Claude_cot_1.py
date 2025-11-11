def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Try each suffix from longest to shortest
    for i in range(len(string) + 1):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Found the longest palindromic suffix
            # Append reverse of the prefix
            prefix = string[:i]
            return string + prefix[::-1]
    
    return string  # Should never reach here
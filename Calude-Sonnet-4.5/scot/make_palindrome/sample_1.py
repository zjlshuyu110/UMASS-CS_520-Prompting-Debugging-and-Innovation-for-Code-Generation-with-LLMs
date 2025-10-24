def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome by checking each suffix.
    """
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Check each suffix from longest to shortest
    for i in range(len(string) + 1):
        if is_palindrome(string[i:]):
            # Found longest palindromic suffix
            # Append reverse of prefix
            return string + string[:i][::-1]
    
    return string
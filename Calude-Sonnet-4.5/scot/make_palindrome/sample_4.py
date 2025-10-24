def make_palindrome(string: str) -> str:
    """
    Start checking from the end and work backwards.
    """
    def check_palindrome(s: str, start: int) -> bool:
        """Check if s[start:] is a palindrome."""
        substr = s[start:]
        return substr == substr[::-1]
    
    # Empty string is already a palindrome
    if not string:
        return string
    
    # Check each starting position
    for start_pos in range(len(string)):
        if check_palindrome(string, start_pos):
            # Need to append reverse of string[:start_pos]
            prefix = string[:start_pos]
            return string + prefix[::-1]
    
    # Entire string is palindrome
    return string
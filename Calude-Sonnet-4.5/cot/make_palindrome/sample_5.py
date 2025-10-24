def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    def find_prefix_length(s: str, start: int = 0) -> int:
        """Find length of prefix to reverse and append."""
        if start > len(s):
            return 0
        if is_palindrome(s[start:]):
            return start
        return find_prefix_length(s, start + 1)
    
    prefix_len = find_prefix_length(string)
    return string + string[:prefix_len][::-1]
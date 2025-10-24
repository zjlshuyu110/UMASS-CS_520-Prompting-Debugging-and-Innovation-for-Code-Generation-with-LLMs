def make_palindrome(string: str) -> str:
    """
    Manually compare characters without creating substring slices for checking.
    """
    def is_suffix_palindrome(s: str, start_idx: int) -> bool:
        """Check if s[start_idx:] is a palindrome without slicing."""
        left = start_idx
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # Find the smallest prefix we need to reverse and append
    for prefix_len in range(len(string) + 1):
        if is_suffix_palindrome(string, prefix_len):
            # Reverse and append the prefix
            return string + string[:prefix_len][::-1]
    
    return string
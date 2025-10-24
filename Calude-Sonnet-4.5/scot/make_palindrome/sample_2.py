def make_palindrome(string: str) -> str:
    """
    Use two-pointer technique to check palindrome validity.
    """
    def is_palindrome_two_pointer(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    i = 0
    while i <= len(string):
        if is_palindrome_two_pointer(string[i:]):
            return string + string[:i][::-1]
        i += 1
    
    return string
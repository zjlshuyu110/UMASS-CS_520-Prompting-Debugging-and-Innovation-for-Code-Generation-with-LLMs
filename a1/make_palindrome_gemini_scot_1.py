def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    # Handles both empty string and standard checks efficiently
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """
    Returns the shortest palindrome that begins with the supplied string by 
    appending the minimal necessary reverse-suffix.

    This is achieved by finding the Longest Palindromic Suffix (LPS), taking 
    the prefix before it, and appending the reverse of that prefix.
    """
    n = len(string)
    if n == 0:
        return ""

    # 1. Find the starting index (i) of the Longest Palindromic Suffix (LPS).
    # We iterate i from 0 upwards. The first string[i:] that is a palindrome 
    # will be the LONGEST palindromic suffix, because we are checking them
    # in order of decreasing length (string[0:], string[1:], ...).
    lps_start_index = n # Default value (no LPS found, but one will be found)
    for i in range(n):
        suffix = string[i:]
        if is_palindrome(suffix):
            lps_start_index = i
            break
    
    # 2. Extract the non-palindromic prefix that needs to be reversed.
    prefix_to_reverse = string[:lps_start_index]
    
    # 3. Reverse the prefix and append it to the original string.
    # If lps_start_index is 0, prefix_to_reverse is "" and we append nothing.
    return string + prefix_to_reverse[::-1]


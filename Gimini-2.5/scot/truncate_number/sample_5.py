import math
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive float using string manipulation.
    This bypasses potential float subtraction errors.
    """
    s = str(number)
    if '.' not in s:
        return 0.0  # Whole number
        
    _, decimal_str = s.split('.', 1)
    
    # If the decimal part is empty (e.g., "3."), return 0.0
    if not decimal_str:
         return 0.0
         
    # Reconstruct the decimal part as a float (e.g., "3.14" -> "0.14")
    try:
        decimal_part = float('0.' + decimal_str)
        # Final check for an edge case where input was a pure whole number 
        # that was auto-formatted to a float (e.g., 3.0 -> "3.0")
        if math.isclose(decimal_part, 0.0) and int(number) == number:
            return 0.0
            
        return decimal_part
    except ValueError:
        return 0.0 # Should not happen for a valid float
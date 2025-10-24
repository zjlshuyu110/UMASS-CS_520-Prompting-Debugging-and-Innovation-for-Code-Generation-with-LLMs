def multiply(a, b):
    """
    Returns the product of the unit digits of a and b.
    Avoids the explicit modulo operator for positive numbers by using a while loop.
    """
    # 1. Get Absolute Values
    a_abs = abs(a)
    b_abs = abs(b)

    # 2/3. Extract Unit Digits without '%' (for positive numbers)
    # The unit digit is a_abs - (a_abs // 10) * 10, which is equivalent to a_abs % 10
    unit_a = a_abs - (a_abs // 10) * 10
    unit_b = b_abs - (b_abs // 10) * 10
    
    # Alternatively, use a loop (less efficient but different logic):
    # a_temp, b_temp = a_abs, b_abs
    # while a_temp >= 10: a_temp -= 10
    # while b_temp >= 10: b_temp -= 10
    # unit_a, unit_b = a_temp, b_temp

    # 4. Calculate Product
    return unit_a * unit_b
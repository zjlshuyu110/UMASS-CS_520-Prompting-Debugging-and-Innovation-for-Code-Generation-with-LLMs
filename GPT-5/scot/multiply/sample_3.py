def multiply(a, b):
    _, a_unit = divmod(abs(a), 10)
    _, b_unit = divmod(abs(b), 10)
    return a_unit * b_unit

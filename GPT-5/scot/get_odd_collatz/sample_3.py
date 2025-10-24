def get_odd_collatz(n):
    seq = [n]
    while seq[-1] != 1:
        last = seq[-1]
        seq.append(3 * last + 1 if last % 2 else last // 2)
    return sorted({x for x in seq if x % 2})

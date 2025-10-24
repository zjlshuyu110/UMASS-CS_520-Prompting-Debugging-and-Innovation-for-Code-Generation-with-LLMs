def multiply(a, b):
    aa = abs(a)
    bb = abs(b)
    ua = aa - (aa // 10) * 10
    ub = bb - (bb // 10) * 10
    return ua * ub

from typing import List, Any

def unique(l: list):
    if not l:
        return []
    s = sorted(l)
    out = [s[0]]
    for x in s[1:]:
        if x != out[-1]:
            out.append(x)
    return out

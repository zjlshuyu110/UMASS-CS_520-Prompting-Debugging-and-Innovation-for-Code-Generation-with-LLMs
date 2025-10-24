from typing import List, Any

def unique(l: list):
    seen = set()
    out = []
    for x in l:
        if x not in seen:
            seen.add(x)
            out.append(x)
    out.sort()
    return out

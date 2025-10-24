from typing import List, Any

def unique(l: list):
    return sorted(dict.fromkeys(l))

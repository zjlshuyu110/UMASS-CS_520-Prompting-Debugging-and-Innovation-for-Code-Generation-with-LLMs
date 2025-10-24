from typing import List, Any
from itertools import groupby

def unique(l: list):
    return [k for k, _ in groupby(sorted(l))]

from typing import List
import math
import bisect

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold <= 0 or len(numbers) < 2:
        return False

    seen: List[float] = []
    dup_infs = set()  # track inf/-inf duplicates

    for x in numbers:
        if math.isnan(x):
            continue
        if math.isinf(x):
            if x in dup_infs:
                return True  # duplicate infinity -> diff 0 < threshold
            dup_infs.add(x)
            continue

        i = bisect.bisect_left(seen, x)
        if i > 0:
            if x == seen[i-1] or x - seen[i-1] < threshold:
                return True
        if i < len(seen):
            if seen[i] == x or seen[i] - x < threshold:
                return True
        seen.insert(i, x)
    return False

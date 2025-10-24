from typing import List, Tuple
import heapq

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Traverse in ascending order using a heap
    h = list(numbers)  # do not mutate original input
    heapq.heapify(h)
    prev = heapq.heappop(h)  # list has at least two elements
    best_pair = (prev, heapq.heappop(h))
    best_diff = best_pair[1] - best_pair[0]
    cur = best_pair[1]
    while h:
        nxt = heapq.heappop(h)
        d = nxt - cur  # non-negative because of ascending pops
        if d < best_diff:
            best_diff = d
            best_pair = (cur, nxt)
        cur = nxt
    return best_pair

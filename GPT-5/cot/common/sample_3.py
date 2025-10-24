def common(l1: list, l2: list):
    """Return a sorted list of unique elements common to both lists."""
    a = sorted(l1)
    b = sorted(l2)
    i = j = 0
    out = []
    last = object()  # sentinel to avoid duplicates in output
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if a[i] != last:
                out.append(a[i])
                last = a[i]
            # advance both, skipping duplicates within each list
            v = a[i]
            while i < len(a) and a[i] == v:
                i += 1
            while j < len(b) and b[j] == v:
                j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out

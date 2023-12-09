def contains_pattern(arr: list[int], m: int, k: int):
    seen = {}
    for i in range(0, len(arr), m):
        fragment = tuple(arr[i: i+m])
        if fragment in seen:
            seen[fragment] += 1
        else:
            seen[fragment] = 1
    max_seen = max(seen.values())
    return max_seen >= k


print(contains_pattern([1, 2, 4, 4, 4, 4], 1, 4))
print(contains_pattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2))
print(contains_pattern([1, 2, 1, 2, 1, 3], 2, 3))
print(contains_pattern([2, 2, 1, 2, 2, 1, 1, 1, 2, 1], 2, 2))
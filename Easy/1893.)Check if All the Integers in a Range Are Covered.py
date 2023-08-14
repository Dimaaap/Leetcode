def is_covered(ranges: list[list[int]], left: int, right: int):
    set_ranges = set(range(left, right + 1))
    intersect_set = []
    for i, j in ranges:
        intersect_set.extend(set_ranges & set(range(i, j + 1)))
    return all([i in set(intersect_set) for i in set_ranges])


print(is_covered([[1, 2], [3, 4], [5, 6]], 2, 5))
print(is_covered([[1, 10], [10, 20]], 21, 21))
print(is_covered([[25, 42], [7, 14], [2, 32], [25, 28], [39, 49], [1, 50], [29, 45], [18, 47]], 18, 38))

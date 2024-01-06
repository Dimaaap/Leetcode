def find_missing_and_repeated_values(grid: list[list[int]]):
    max_num = len(grid) ** 2 + 1
    seen = {}
    missing = repeated = None
    for i in grid:
        for j in i:
            if j not in seen:
                seen[j] = 1
            else:
                seen[j] += 1
    for k in range(1, max_num):
        if k not in seen:
            missing = k
        elif seen[k] == 2:
            repeated = k
    return [repeated, missing]


print(find_missing_and_repeated_values([[1, 3], [2, 2]]))
print(find_missing_and_repeated_values([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))

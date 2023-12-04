def lucky_numbers(matrix: list[list[int]]):
    mins = {min(i) for i in matrix}
    maxs = {max(i) for i in zip(*matrix)}
    return list(set(maxs) & set(mins))


print(lucky_numbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(lucky_numbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(lucky_numbers([[7, 8], [1, 2]]))

def count_negatives(grid: list[list[int]]):
    counter = 0
    for i in grid:
        for j in i:
            if j < 0:
                counter += 1
    return counter


print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(count_negatives([[3, 2], [0, 1]]))
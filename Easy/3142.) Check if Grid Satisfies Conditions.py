def satisfies_conditions(grid: list[list[int]]):
    """
    You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
        Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
        Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
    Return true if all the cells satisfy these conditions, otherwise, return false.
    """
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            try:
                if grid[i][j] != grid[i + 1][j]:
                    return False
            except IndexError:
                pass
            try:
                if grid[i][j] == grid[i][j + 1]:
                    return False
            except IndexError:
                pass
    return True


print(satisfies_conditions([[1, 0, 2], [1, 0, 2]]))
print(satisfies_conditions([[1, 1, 1], [0, 0, 0]]))
print(satisfies_conditions([[1], [2], [3]]))
print(satisfies_conditions([[1, 1, 6, 1, 4, 6, 3, 1, 0, 7]]))
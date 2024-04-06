def largest_local(grid: list[list[int]]):
    """
    You are given an n x n integer matrix grid.
    Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
        maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

    In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
    Return the generated matrix.
    """
    n = len(grid)
    ans = [[1] * (n - 2) for i in range(n - 2)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            ans[i - 1][j - 1] = max(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                                       grid[i][j - 1], grid[i][j], grid[i][j + 1],
                                       grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1])
    return ans


print(largest_local([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(largest_local(
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
))
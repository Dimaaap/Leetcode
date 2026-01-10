def reverse_submatrix(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    """
    You are given an m x n integer matrix grid, and three integers x, y, and k.
    The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k
    represents the size (side length) of the square submatrix.

    Your task is to flip the submatrix by reversing the order of its rows vertically.
    Return the updated matrix.
    """

    block = grid[x:x + k]
    for i in range(len(block)):
        block[i] = block[i][y:y+k]

    rows = len(block)
    cols = len(block[0])

    for r in range(rows // 2):
        for c in range(cols):
            block[r][c], block[rows - 1 - r][c] = block[rows - 1 - r][c], block[r][c]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i < x or i >= x + k or j < y or j >= y + k:
                continue
            else:
                grid[i][j] = block[i - x][j - y]
    return grid


print(reverse_submatrix([[1,2,3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1, 0, 3))
print(reverse_submatrix([[3, 4, 2, 3], [2, 3, 4, 2]], 0, 2, 2))
print(reverse_submatrix([[14, 3, 18, 16], [2, 14, 11, 20], [19, 19, 4, 15], [11, 15, 18, 6]], 0, 0, 4))

def minimum_area(grid: list[list[int]]) -> int:
    """
    You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the
    smallest area, such that all the 1's in grid lie inside this rectangle.

    Return the minimum possible area of the rectangle.
    """
    min_row, min_col = float("inf"), float("inf")
    max_row, max_col = 0, 0
    grid_len = len(grid)
    row_len = len(grid[0])

    for i in range(grid_len):
        for j in range(row_len):
            if grid[i][j] == 1:
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    height = max_row - min_row + 1
    width = max_col - min_col + 1
    return height * width


print(minimum_area([[0, 1, 0], [1, 0, 1]]))
print(minimum_area([[1, 0], [0, 0]]))
print(minimum_area([[0], [1]]))
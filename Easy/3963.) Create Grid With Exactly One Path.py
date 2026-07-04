def create_grid(m: int, n: int) -> list[str]:
    """
    You are given two integers m and n, representing the number of rows and columns of a grid.
    Construct any m x n grid consisting only of the characters '.' and '#', where:
    '.' represents a free cell.
    '#' represents an obstacle cell.
    A valid path is a sequence of free cells that:
        Starts at the top-left cell (0, 0).
        Ends at the bottom-right cell (m - 1, n - 1).
    Moves only:
        Right, from (i, j) to (i, j + 1), or
        Down, from (i, j) to (i + 1, j).
    Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.
    """

    free_cell = "."
    obstacle_cell = "#"

    grid = []

    for i in range(m):
        row = ""
        for j in range(n):
            if i == 0 or j == n - 1:
                row += free_cell
            else:
                row += obstacle_cell
        grid.append(row)

    return grid


print(create_grid(2, 3))
print(create_grid(3, 3))
print(create_grid(1, 4))
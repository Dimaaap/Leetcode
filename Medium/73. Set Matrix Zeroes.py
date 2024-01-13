def set_zeroes(matrix: list[list[int]]):
    """
    Given an m x n integer matrix matrix, if an element is 0,
    set its entire row and column to 0's.
    You must do it in place.
    """
    first_col = False
    m, n = len(matrix), len(matrix[0])

    for r in range(m):
        if matrix[r][0] == 0:
            first_col = True

        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for c in range(n):
            matrix[0][c] = 0
    if first_col:
        for r in range(m):
            matrix[r][0] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix_second = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

set_zeroes(matrix)
set_zeroes(matrix_second)
print(matrix)
print(matrix_second)

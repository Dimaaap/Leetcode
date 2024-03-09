def check_x_matrix(grid: list[list[int]]):
    """
    A square matrix is said to be an X-Matrix if both of the following conditions hold:
        1) All the elements in the diagonals of the matrix are non-zero.
        2) All other elements are 0.
    Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix.
    Otherwise, return false.
    """
    if check_matrix_diagonals(grid):
        matrix_len = len(grid)
        for i in range(matrix_len):
            for j in range(matrix_len):
                if i != j and i != matrix_len - j - 1:
                    if grid[i][j] != 0:
                        return False
        return True
    return False


def check_matrix_diagonals(matrix: list[list[int]]):
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for j in range(matrix_len):
            if i == j and matrix[i][j] == 0:
                return False
            if i == matrix_len - j - 1 and matrix[i][j] == 0:
                return False
    return True


print(check_x_matrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
print(check_x_matrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]))

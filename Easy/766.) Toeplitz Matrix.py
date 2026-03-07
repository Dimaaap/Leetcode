def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    """
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
    """

    n = len(matrix)
    m = len(matrix[0])

    for i in range(1, n):
        for j in range(1, m ):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


print(is_toeplitz_matrix([
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]))

print(is_toeplitz_matrix([
    [1, 2], [2, 2]
]))
def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    """
    In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a
    different size r x c keeping its original data.

    You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of
    columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original matrix in the same
    row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
    Otherwise, output the original matrix.
    """
    matrix_len = len(mat) * len(mat[0])
    reshape_matrix_len = r * c
    if matrix_len != reshape_matrix_len:
        return mat

    flat_mat = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            flat_mat.append(mat[i][j])

    res = []
    flat_iter = iter(flat_mat)
    for i in range(r):
        new_row = []
        for j in range(c):
            new_row.append(next(flat_iter))
        res.append(new_row)
    return res


print(matrix_reshape([[1, 2], [3, 4]], 1, 4))
print(matrix_reshape([[1, 2], [3, 4]], 2, 4))
print(matrix_reshape([[1, 2, 3, 4]], 2, 2))
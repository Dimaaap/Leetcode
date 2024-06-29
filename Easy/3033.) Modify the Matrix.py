def modified_matrix(matrix: list[list[int]]):
    m, n = len(matrix), len(matrix[0])
    transpose = list(map(list, zip(*matrix)))

    for i in range(n):
        mx = max(transpose[i])
        for j in range(m):
            if transpose[i][j] != -1:
                continue
            transpose[i][j] = mx

    return zip(*transpose)


print(modified_matrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]))

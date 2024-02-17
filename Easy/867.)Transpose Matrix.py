def transpose(matrix: list[list[int]]):
    ans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return ans


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
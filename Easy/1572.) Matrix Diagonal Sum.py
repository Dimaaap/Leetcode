def diagonal_sum(mat: list[list[int]]):
    main_d = help_d = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                main_d += mat[i][j]
            if j == len(mat[0]) - i - 1:
                help_d += mat[i][j]
    if len(mat) % 2 != 0:
        mid_el = len(mat) // 2
        return main_d + help_d - mat[mid_el][mid_el]
    return main_d + help_d


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonal_sum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(diagonal_sum([[5]]))

def k_weakest_rows(mat: list[list[int]], k: int):
    soldiers_count = {}
    for row in range(len(mat)):
        soldiers_count[row] = mat[row].count(1)
    sorted_soldiers = sorted(soldiers_count.items(), key=lambda x: x[1])
    result_list = [i for i, j in sorted_soldiers][:k]
    return result_list


print(k_weakest_rows([[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]], 3))
print(k_weakest_rows([[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]], 2))
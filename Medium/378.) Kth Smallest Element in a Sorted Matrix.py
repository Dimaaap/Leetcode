def kth_smallest(matrix: list[list[int]], k: int):
    common_list = [j for i in matrix for j in i]
    return sorted(common_list)[k - 1]


print(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(kth_smallest([[-5]], 1))

def row_and_maximum_ones(mat: list[list[int]]):
    """
    Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones,
    and the number of ones in that row. In case there are multiple rows that have the maximum count of ones, the
    row with the smallest row number should be selected. Return an array containing the index of the row, and the
    number of ones in it.
    """
    count_list = []
    for i in mat:
        count_ones = i.count(1)
        count_list.append([mat.index(i), count_ones])
    if len({i[-1] for i in count_list}) == 1:
        return count_list[0]
    return max(count_list)


print(row_and_maximum_ones([[0, 1], [1, 0]]))
print(row_and_maximum_ones([[0, 0, 0], [0, 1, 1]]))
print(row_and_maximum_ones([[0, 0], [1, 1], [0, 0]]))
print()

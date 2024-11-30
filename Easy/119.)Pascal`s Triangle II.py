def get_row(row_index: int) -> list[int]:
    """
    Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    """
    start_list = [[1], [1, 1]]
    if row_index in (0, 1):
        return start_list[row_index]
    i = 2
    while i <= row_index:
        new_row = [1]
        last_done_row = start_list[-1]
        for j in range(0, len(last_done_row) - 1):
            new_row.append(last_done_row[j] + last_done_row[j+1])
        new_row.append(1)
        start_list.append(new_row)
        i += 1
    return start_list[row_index]


print(get_row(3))
print(get_row(0))
print(get_row(1))


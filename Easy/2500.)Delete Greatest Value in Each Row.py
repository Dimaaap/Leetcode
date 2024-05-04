def delete_greatest_value(grid: list[list[int]]):
    """
    You are given an m x n matrix grid consisting of positive integers.
    Perform the following operation until grid becomes empty:
    Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
    Add the maximum of deleted elements to the answer.
    Note that the number of columns decreases by one after each operation.
    Return the answer after performing the operations described above.
    """
    n = len(grid)
    ans = 0
    while not all(i == [] for i in grid):
        max_rows = -100
        for i in range(n):
            max_row = max(grid[i])
            grid[i].remove(max_row)
            max_rows = max(max_row, max_rows)
        ans += max_rows
    return ans


print(delete_greatest_value([[1, 2, 4], [3, 3, 1]]))
print(delete_greatest_value([[10]]))
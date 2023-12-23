def delete_greatest_value(grid: list[list[int]]):
    ans = 0
    while grid:
        for i in range(len(grid)):
            ans += max(grid[i])
            grid.remove(grid[i])
    return ans


print(delete_greatest_value([[1, 2, 4], [3, 3, 1]]))

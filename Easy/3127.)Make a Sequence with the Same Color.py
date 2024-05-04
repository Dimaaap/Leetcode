def can_make_square(grid: list[list[str]]):
    for rows in range(3):
        for cols in range(3):
            if rows < 2:
                square_list = grid[rows][cols: cols + 2] + grid[rows + 1][cols: cols + 2]
                if len(square_list) == 4 and (square_list.count("W") <= 1 or square_list.count("B") <= 1):
                    return True
    return False


print(can_make_square([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
print(can_make_square([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
print(can_make_square([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]))
print(can_make_square([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))

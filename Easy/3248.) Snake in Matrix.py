def final_position_of_snake(n: int, commands: list[str]) -> int:
    matrix = []
    k = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(k)
            k += 1
        matrix.append(row)
    start_row, start_col = 0, 0
    for command in commands:
        if command == "RIGHT":
            start_col += 1
        if command == "DOWN":
            start_row += 1
        if command == "LEFT":
            start_col -= 1
        if command == "UP":
            start_row -= 1
    return matrix[start_row][start_col]


print(final_position_of_snake(2, ["RIGHT", "DOWN"]))
print(final_position_of_snake(3, ["DOWN", "RIGHT", "UP"]))

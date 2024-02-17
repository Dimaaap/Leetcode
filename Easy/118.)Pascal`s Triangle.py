def generate(num_rows: int):
    start_arr = [[1], [1, 1]]
    if num_rows < 3:
        return start_arr[:num_rows]
    for _ in range(num_rows - 2):
        next_row = [1]
        for i in range(1, len(start_arr[-1])):
            next_row.append(start_arr[-1][i] + start_arr[-1][i-1])
        next_row += [1]
        start_arr.append(next_row)
    return start_arr


print(generate(5))
print(generate(1))
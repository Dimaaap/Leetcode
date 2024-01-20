def daily_temperatures(temperatures: list[int]):
    stack = []
    output = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            _, old_idx = stack.pop()
            output[old_idx] = i - old_idx
        stack.append((temp, i))
    return output


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
def busy_student(start_time: list[int], end_time: list[int], query_time: int):
    counter = 0
    for (i, j) in zip(start_time, end_time):
        if i <= query_time <= j:
            counter += 1
    return counter


print(busy_student([1, 2, 3], [3, 2, 7], 4))
print(busy_student([4], [4], 4))
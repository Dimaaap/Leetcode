def number_of_employees_who_met_target(hours: list[int], target: int):
    counter = 0
    for i in hours:
        if i >= target:
            counter += 1
    return counter


print(number_of_employees_who_met_target([0, 1, 2, 3, 4], 2))
print(number_of_employees_who_met_target([5, 1, 4, 2, 2, ], 6))
def sum_of_multiplies(n: int):
    nums_sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            nums_sum += i
    return nums_sum


print(sum_of_multiplies(7))
print(sum_of_multiplies(10))
print(sum_of_multiplies(9))

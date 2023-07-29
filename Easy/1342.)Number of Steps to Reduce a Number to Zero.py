def number_of_steps(num: int):
    count_steps = 0
    while num:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        count_steps += 1
    return count_steps


print(number_of_steps(14))
print(number_of_steps(8))
print(number_of_steps(123))

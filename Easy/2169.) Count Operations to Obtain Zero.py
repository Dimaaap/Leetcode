def count_operations(num1: int, num2: int):
    counter = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        counter += 1
    return counter


print(count_operations(2, 3))
print(count_operations(10, 10))
def the_maximum_achievable_x(num: int, t: int):
    while t:
        num += 2
        t -= 1
    return num


print(the_maximum_achievable_x(4, 1))
print(the_maximum_achievable_x(3, 2))
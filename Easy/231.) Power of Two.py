def is_power_of_two(n: int):
    counter = 1
    while counter < n:
        counter *= 2
    return counter == 2



print(is_power_of_two(536870913))
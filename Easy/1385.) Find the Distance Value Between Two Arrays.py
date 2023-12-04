def find_the_distance_value(arr1: list[int], arr2: list[int], d: int):
    counter = 0
    for i in arr1:
        if all(abs(i - j) > d for j in arr2):
            counter += 1
    return counter


print(find_the_distance_value([4, 5, 8], [10, 9, 1, 8], 2))
print(find_the_distance_value([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(find_the_distance_value([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))

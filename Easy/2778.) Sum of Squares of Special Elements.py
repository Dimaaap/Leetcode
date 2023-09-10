def sum_of_squares(nums: list[int]):
    l = len(nums)
    result = 0
    for index, element in enumerate(nums):
        if l % (index + 1) == 0:
            result += (element ** 2)
    return result


print(sum_of_squares([1, 2, 3, 4]))
print(sum_of_squares([2, 7, 1, 19, 18, 3]))

def sorted_squares(nums: list[int]):
    return sorted([i ** 2 for i in nums])


print(sorted_squares([-4, -1, 0, 3, 10]))
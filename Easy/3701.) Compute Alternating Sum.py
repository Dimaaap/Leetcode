def alternating_sum(nums: list[int]) -> int:
    res = 0
    for index, num in enumerate(nums):
        if index % 2 == 0:
            res += num
        else:
            res -= num
    return res


print(alternating_sum([1, 3, 5, 7]))
print(alternating_sum([100]))
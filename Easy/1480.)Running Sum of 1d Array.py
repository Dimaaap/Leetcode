def running_sum(nums: list[int]):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums


print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
def minimum_operations(nums: list[int]) -> int:
    counter = 0
    while len(set(nums)) != 1:
        min_num = min(i for i in nums if i != 0)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] -= min_num
        counter += 1
    return counter


print(minimum_operations([1, 5, 0, 3, 5]))
print(minimum_operations([0]))
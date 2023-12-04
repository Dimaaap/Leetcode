def minimum_operations(nums: list[int]):
    if len(nums) == 1 and nums[0] != 0:
        return 1
    counter = 0
    while nums.count(0) != len(nums):
        nums_without_zero = [i for i in nums if i != 0]
        min_nums = min(nums_without_zero)
        nums = [i - min_nums for i in nums if i != 0]
        counter += 1
    return counter


print(minimum_operations([1, 5, 0, 3, 5]))
print(minimum_operations([0]))
print(minimum_operations([1]))
print(minimum_operations(
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100]))

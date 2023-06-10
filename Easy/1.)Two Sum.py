def two_sum(nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    """
    subtract_index = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in subtract_index:
            return [subtract_index[diff], index]
        subtract_index[value] = index


def two_sum_second(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

print(two_sum_second([2, 7, 11, 15], 9))
print(two_sum_second([3, 2, 4], 6))
print(two_sum_second([3, 3], 6))

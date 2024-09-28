def min_start_value(nums: list[int]) -> int:
    """
    Given an array of integers nums, you start with an initial positive value startValue.

    In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

    Return the minimum positive value of startValue such that the step by step sum is never less than 1.
    """
    min_sum = 1
    new_sum = 0

    for num in nums:
        new_sum += num
        min_sum = min(min_sum, new_sum)
    if min_sum < 0:
        return abs(min_sum) + 1
    return 1


print(min_start_value([-3, 2, -3, 4, 2]))
print(min_start_value([1, 2]))
print(min_start_value([1, -2, -3]))
print(min_start_value([1, -1]))
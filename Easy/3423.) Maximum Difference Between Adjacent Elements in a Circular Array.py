def max_adjacent_distance(nums: list[int]) -> int:
    """
    Given a circular array nums, find the maximum absolute difference between adjacent elements.
    Note: In a circular array, the first and last elements are adjacent.
    """

    first_last_diff = abs(nums[-1] - nums[0])
    res = first_last_diff

    i = 1
    while i < len(nums):
        diff = abs(nums[i] - nums[i - 1])
        res = max(res, diff)
        i += 1
    return res


print(max_adjacent_distance([1, 2, 4]))
print(max_adjacent_distance([-5, -10, -5]))
print(max_adjacent_distance([-2, 1, -5]))
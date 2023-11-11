def get_min_distance(nums: list[int], target: int, start: int):
    """
    Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] ==
    target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
    Return abs(i - start).
    It is guaranteed that target exists in nums.
    """
    x = []
    for i in range(len(nums)):
        if nums[i] == target:
            x.append(abs(i - start))
    return min(x)


print(get_min_distance([1, 2, 3, 4, 5], 5, 3))
print(get_min_distance([1], 1, 0))
print(get_min_distance([1, 1, 1, 1, 1, 1, 1], 1, 0))
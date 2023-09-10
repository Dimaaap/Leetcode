def count_pairs(nums: list[int], target: int):
    """
    Given a 0-indexed integer array nums of length n and an integer target,
    return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
    """
    counter = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                counter += 1
    return counter


print(count_pairs([-1, 1, 2, 3, 1], 2))
print(count_pairs([-6, 2, 5, -2, -7, -1, 3], -2))


def minimum_difference(nums: list[int], k: int):
    """
    You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
    You are also given an integer k.
    Pick the scores of any k students from the array so that the difference between the highest and
    the lowest of the k scores is minimized.
    Return the minimum possible difference.
    """
    nums.sort()
    l, r = 0, k - 1
    res = float("inf")
    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        l += 1
        r += 1
    return res


print(minimum_difference([90], 1))
print(minimum_difference([9, 4, 1, 7], 2))
print(minimum_difference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6))

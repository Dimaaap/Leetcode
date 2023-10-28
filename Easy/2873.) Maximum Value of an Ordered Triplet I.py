def maximum_triplet_value(nums: list[int]):
    """
    You are given a 0-indexed integer array nums.
    Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a
    negative value, return 0. The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
    """
    ans = diff = prefix = 0
    for i in nums:
        ans = max(ans, i * diff)
        diff = max(diff, prefix - i)
        prefix = max(prefix, i)
    return ans


print(maximum_triplet_value([12, 6, 1, 2, 7]))
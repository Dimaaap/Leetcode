def missing_integer(nums: list[int]):
    """
    You are given a 0-indexed array of integers nums.
    A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1.
     In particular, the prefix consisting only of nums[0] is sequential.
    Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the
    longest sequential prefix.
    """
    count = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            count += nums[i]
        else:
            break
    while True:
        if count not in nums:
            return count
        else:
            count += 1



print(missing_integer([1, 2, 3, 2, 5]))
print(missing_integer([3, 4, 5, 1, 12, 14, 13]))
print(missing_integer([29, 30, 31, 32, 33, 34, 35, 36, 37]))
print(missing_integer([1, 4, 3]))
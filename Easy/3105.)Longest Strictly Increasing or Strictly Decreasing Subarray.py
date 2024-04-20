def longest_monotonic_subarray(nums: list[int]):
    """
    You are given an array of integers nums. Return the length of the longest subarray of nums which is either
    strictly increasing or strictly decreasing.
    """
    incr, decr, ans = 1, 1, 1
    prev= nums.pop(0)

    for num in nums:
        incr = incr * (num > prev) + 1
        decr = decr * (num < prev) + 1
        prev = num
        ans = max(ans, incr, decr)
    return ans



print(longest_monotonic_subarray([1, 4, 3, 3, 2]))
print(longest_monotonic_subarray([3, 3, 3, 3]))



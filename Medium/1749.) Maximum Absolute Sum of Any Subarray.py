def max_absolute_sum(nums: list[int]) -> int:
    """
    You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is
    abs(numsl + numsl+1 + ... + numsr-1 + numsr).

    Return the maximum absolute sum of any (possibly empty) subarray of nums.

    Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.
    """
    max_ending = min_ending = 0
    max_sum = min_sum = 0

    for n in nums:
        max_ending = max(n, max_ending + n)
        max_sum = max(max_sum, max_ending)

        min_ending = min(n, min_ending + n)
        min_sum = min(min_sum, min_ending)

    return max(abs(max_sum), abs(min_sum))


# print(max_absolute_sum([1, -3, 2, 3, -4]))
print(max_absolute_sum([2, -5, 1, -4, 3, -2]))

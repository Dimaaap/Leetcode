def count_partitions(nums: list[int]) -> int:
    """
    You are given an integer array nums of length n.
    A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty
    subarrays such that:

    Left subarray contains indices [0, i].
    Right subarray contains indices [i + 1, n - 1].

    Return the number of partitions where the difference between the sum of the left and right subarrays is even.
    """
    i = 1
    count = 0
    while i < len(nums):
        left, right = nums[:i], nums[i:]
        sum_left, sum_right = sum(left), sum(right)
        if abs(sum_left - sum_right) % 2 == 0:
            count += 1
        i += 1
    return count


print(count_partitions([10, 10, 3, 7, 6]))
print(count_partitions([1, 2, 2]))
print(count_partitions([2, 4, 6, 8]))
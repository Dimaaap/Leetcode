def min_operations(nums: list[int]) -> int:
    """
    You are given an integer array nums of length n.
    In one operation, choose any subarray nums[l...r] (0 <= l <= r < n) and replace each element in that
    subarray with the bitwise AND of all elements.
    Return the minimum number of operations required to make all elements of nums equal.
    A subarray is a contiguous non-empty sequence of elements within an array.
    """

    if len(set(nums)) == 1:
        return 0
    return 1


print(min_operations([1, 2]))
print(min_operations([5, 5, 5]))
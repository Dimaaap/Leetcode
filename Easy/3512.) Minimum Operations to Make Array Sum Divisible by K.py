def min_operations(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k. You can perform the following operation any number of times:

    Select an index i and replace nums[i] with nums[i] - 1.
    Return the minimum number of operations required to make the sum of the array divisible by k.
    """
    modulo = sum(nums) % k
    return modulo


print(min_operations([3, 9, 7], 5))
print(min_operations([4, 1, 3], 4))
print(min_operations([3, 2], 6))
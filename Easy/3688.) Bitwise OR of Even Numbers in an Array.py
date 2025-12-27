def even_numbers_bitwise_or(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    Return the bitwise OR of all even numbers in the array.
    If there are no even numbers in nums, return 0.
    """
    res = 0
    for num in nums:
        if num % 2 == 0:
            res |= num
    return res


print(even_numbers_bitwise_or([1, 2, 3, 4, 5, 6]))
print(even_numbers_bitwise_or([7, 9, 11]))
print(even_numbers_bitwise_or([1, 8, 16]))
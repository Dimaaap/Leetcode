def duplicate_numbers_xor(nums: list[int]) -> int:
    """
    You are given an array nums, where each number in the array appears either once or twice.

    Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
    """
    res = 0
    seen = set()
    for num in nums:
        if num in seen:
            res ^= num
        else:
            seen.add(num)
    return res


print(duplicate_numbers_xor([1, 2, 1, 3]))
print(duplicate_numbers_xor([1, 2, 3]))
print(duplicate_numbers_xor([1, 2, 2, 1]))
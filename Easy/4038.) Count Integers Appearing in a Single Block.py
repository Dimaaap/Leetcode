def count_special_integers(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    An integer x is special if all occurrences of x in nums appear in a single contiguous block.
    Return the number of distinct special integers in nums.
    """

    counter = 0
    seen = set()
    i = 0

    while i < len(nums):
        num = nums[i]
        first = i
        last = len(nums) - (nums[::-1].index(num)) - 1
        if last - first + 1 == nums.count(num) and num not in seen:
            counter += 1
            i = last + 1
        else:
            i += 1
        seen.add(num)
    return counter



print(count_special_integers([1, 2, 2, 1]))
print(count_special_integers([3, 3, 1, 2, 2, 1]))
print(count_special_integers([30, 30, 30, 40, 38, 30]))
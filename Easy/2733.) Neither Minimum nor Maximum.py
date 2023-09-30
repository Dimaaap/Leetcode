def find_non_min_or_max(nums: list[int]):
    """
    Given an integer array nums containing distinct positive integers, find and return any number from
    the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
    Return the selected integer.
    """
    min_num, max_num = min(nums), max(nums)
    for i in nums:
        if i != min_num and i != max_num:
            return i
    return -1


print(find_non_min_or_max([3, 2, 1, 4]))
print(find_non_min_or_max([1, 2]))
print(find_non_min_or_max([2, 1 ,3]))
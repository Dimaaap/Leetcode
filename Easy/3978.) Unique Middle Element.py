def is_middle_element_unique(nums: list[int]) -> bool:
    """
    You are given an integer array nums of odd length n.
    Return true if the middle element of nums appears exactly once in the array. Otherwise return false.
    """

    middle_index = int((len(nums) - 1) / 2)

    if nums.count(nums[middle_index]) != 1:
        return False
    return True


print(is_middle_element_unique([1, 2, 3]))
print(is_middle_element_unique([1, 2, 2]))
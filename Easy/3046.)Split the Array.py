def is_possible_to_split(nums: list[int]):
    """
    You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2
    such that:
        nums1.length == nums2.length == nums.length / 2.
        nums1 should contain distinct elements.
        nums2 should also contain distinct elements.
    Return true if it is possible to split the array, and false otherwise.
    """
    nums_set = set(nums)
    for num in nums_set:
        if nums.count(num) > 2:
            return False
    return True


print(is_possible_to_split([1, 1, 2, 2, 3, 4]))
print(is_possible_to_split([1, 1, 1, 1]))
print(is_possible_to_split([6, 1, 3, 1, 1, 8, 9, 1]))


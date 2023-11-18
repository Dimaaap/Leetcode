def get_common(nums1: list[int], nums2: list[int]):
    """
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to
    both arrays. If there is no common integer amongst nums1 and nums2, return -1.
    Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of
    that integer.
    """
    common_set = set(nums1) & set(nums2)
    if common_set:
        return min(common_set)
    return -1


print(get_common([1, 2, 3], [2, 4]))
print(get_common([1, 2, 3, 6], [2, 3, 4, 5]))
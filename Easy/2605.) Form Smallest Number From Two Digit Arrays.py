def min_number(nums1: list[int], nums2: list[int]) -> int:
    """
    Given two arrays of unique digits nums1 and nums2, return the smallest number that
    contains at least one digit from each array.
    """
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    if not (set(nums1) & set(nums2)):
        return min(int(str(nums1[0]) + str(nums2[0])), int(str(nums2[0]) + str(nums1[0])))
    else:
        return sorted(list(set(nums1) & set(nums2)))[0]


print(min_number([4, 1, 3], [5, 7]))
print(min_number([3, 5, 2, 6], [3, 1, 7]))
print(min_number([5, 8, 2, 7], [5, 2, 8, 4, 7, 1, 3]))
print(min_number([7, 5, 6], [1, 4]))
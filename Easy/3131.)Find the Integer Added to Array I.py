def added_integer(nums1: list[int], nums2: list[int]):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    return nums2[0] - nums1[0]


print(added_integer([2, 6, 4], [9, 7, 5]))
print(added_integer([10], [5]))

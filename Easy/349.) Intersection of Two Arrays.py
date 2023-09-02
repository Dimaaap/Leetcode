def intersection(nums1: list[int], nums2: list[int]):
    return set(nums1) & set(nums2)


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
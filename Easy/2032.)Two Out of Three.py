def two_out_of_three(nums1: list[int], nums2: list[int], nums3: list[int]):
    ans = []
    first_intersect = set(nums1) & set(nums2)
    ans.extend(list(first_intersect))
    ans.extend(set(nums2) & set(nums3))
    ans.extend(set(nums1) & set(nums3))
    return list(set(ans))


print(two_out_of_three([1, 1, 3, 2], [2, 3], [3]))
print(two_out_of_three([3, 1], [2, 3], [1, 2]))
print(two_out_of_three([1, 2, 2], [4, 3, 3], [5]))
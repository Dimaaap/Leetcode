def intersect(nums1: list[int], nums2: list[int]):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays and you may
    return the result in any order.
    """
    ans = []
    for i in nums1:
        if i in nums2:
            ans.append(i)
            nums2.remove(i)
    return ans


print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
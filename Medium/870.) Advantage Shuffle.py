def advantage_count(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    You are given two integer arrays nums1 and nums2 both of the same length. The advantage of
    nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
    Return any permutation of nums1 that maximizes its advantage with respect to nums2.
    """

    nums1 = sorted(nums1)
    nums2_sorted = sorted([(value, index) for index, value in enumerate(nums2)])

    result = [0] * len(nums2)

    left = 0
    right = len(nums2) - 1

    for num in nums1:
        if num > nums2_sorted[left][0]:
            value, index = nums2_sorted[left]
            result[index] = num
            left += 1
        else:
            value, index = nums2_sorted[right]
            result[index] = num
            right -= 1
    return result

print(advantage_count([2, 7, 11, 15], [1, 10, 4, 11]))
print(advantage_count([12, 24, 8, 32], [13, 25, 32, 11]))


def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    """

    a, b, write_index = m - 1, n - 1, m + n - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[write_index] = nums1[a]
            a -= 1
        else:
            nums1[write_index] = nums2[b]
            b -= 1
        write_index -= 1
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
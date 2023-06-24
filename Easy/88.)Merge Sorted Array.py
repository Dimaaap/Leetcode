def merge(nums: list[int], m: int, nums2: list[int], n: int):
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    """

    final_list = []
    i, j = 0, 0
    nums_m = nums[:m]
    nums_n = nums2[:n]
    while i < m and j < n:
        if nums_m[i] < nums_n[j]:
            print(nums_m[i], i)
            final_list.append(nums_m[i])
            i += 1
        else:
            print(nums_n[j], j)
            final_list.append(nums_n[j])
            j += 1
    if i < m:
        final_list += nums_m[i:m]
    elif j < n:
        final_list += nums_n[j:n]
    return final_list


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
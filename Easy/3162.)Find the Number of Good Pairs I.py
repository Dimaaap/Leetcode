def number_of_pairs(nums1: list[int], nums2: list[int], k:int) -> int:
    """
    You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively.
    You are also given a positive integer k.

    A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

    Return the total number of good pairs.
    """
    nums2 = [i * k for i in nums2]
    counter = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % nums2[j] == 0:
                counter += 1
    return counter


print(number_of_pairs([1, 3, 4], [1, 3, 4], 1))
print(number_of_pairs([1, 2, 4, 12], [2, 4], 3))
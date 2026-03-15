def min_sum(nums1: list[int], nums2: list[int]) -> int:
    """
    You are given two arrays nums1 and nums2 consisting of positive integers.
    You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of
    both arrays becomes equal.
    Return the minimum equal sum you can obtain, or -1 if it is impossible.
    """
    counter_0_1 = nums1.count(0)
    counter_0_2 = nums2.count(0)

    sum1 = sum(nums1)
    sum2 = sum(nums2)

    min_sum1 = sum1 + counter_0_1
    min_sum2 = sum2 + counter_0_2

    if counter_0_1 == 0 and min_sum1 < min_sum2:
        return -1
    if counter_0_2 == 0 and min_sum2 < min_sum1:
        return -1

    return max(min_sum1, min_sum2)


print(min_sum([3, 2, 0, 1, 0], [6, 5, 0]))
print(min_sum([2, 0, 2, 0], [1, 4]))
print(min_sum([9, 5], [15, 12 ,5, 21, 4, 26, 27, 9, 6, 29, 0, 18, 16, 0, 0, 0, 20]))
print(min_sum([0, 0], [29, 28]))
print(min_sum([12, 14, 25, 12, 3], [3, 26, 0, 21, 22]))
print(min_sum([25, 29, 10, 12, 25, 26, 19, 6, 19, 10, 18],
              [0, 0, 22, 2, 17, 0, 7, 23, 22, 18, 20, 0, 13, 22, 0, 0, 0, 13 ,6, 8]))
print(min_sum([10, 4, 24, 2, 17, 10, 0, 29, 3, 0, 19, 7, 24, 17, 30, 7],
              [1, 0, 13, 0, 0, 28, 0, 23, 24, 13, 4, 30, 8, 4, 0, 1, 29, 25]))
print(min_sum([8, 13, 15, 18, 0, 18, 0, 0, 5, 20, 12, 27, 3, 14, 22, 0],
              [29, 1, 6, 0, 10, 24, 27, 17, 14, 13, 2, 19, 2, 11]))
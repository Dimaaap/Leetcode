def find_intersection_values(nums1: list[int], nums2: list[int]):
    count1 = count2 = 0
    for index, element in enumerate(nums1):
        if element in nums2:
            count1 += 1
    for index, element in enumerate(nums2):
        if element in nums1:
            count2 += 1
    return [count1, count2]


print(find_intersection_values([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))
print(find_intersection_values([3, 4, 2, 3], [1, 5]))


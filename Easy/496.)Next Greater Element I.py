def next_greater_element(nums1: list[int], nums2: list[int]):
    res = []
    for index, num in enumerate(nums1):
        num2_index = nums2.index(num)
        for j in nums2[num2_index+1:]:
            if j > num:
                res.append(j)
                break
        else:
            res.append(-1)
    return res


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_element([2, 4], [1, 2, 3, 4]))
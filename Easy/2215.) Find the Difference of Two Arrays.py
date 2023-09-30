def find_difference(nums1: list[int], nums2: list[int]):
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.
    """
    ans = []
    ans.append(list(set(nums1) - set(nums2)))
    ans.append(list(set(nums2) - set(nums1)))
    return ans


print(find_difference([1, 2, 3], [2, 4, 6]))
print(find_difference([1, 2, 3, 3], [1, 1, 2, 2]))

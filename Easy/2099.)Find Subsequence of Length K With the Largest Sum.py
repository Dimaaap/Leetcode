def max_subsequence(nums: list[int], k: int):
    i = 0
    result_list = []
    while i < k:
        max_element = max(nums)
        result_list.append(max_element)
        nums.remove(max_element)
        i += 1
    return result_list[::-1]


print(max_subsequence([2, 1, 3, 3], 2))
print(max_subsequence([-1, -2, 3, 4], 3))
print(max_subsequence([3, 4, 3, 3], 2))

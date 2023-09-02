def find_kth_largest(nums: list[int], k: int):
    sorted_list = sorted(nums)[::-1]
    return sorted_list[k-1]


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
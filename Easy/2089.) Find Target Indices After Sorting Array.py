def target_indices(nums: list[int], target: int):
    nums = sorted(nums)
    return nums


print(target_indices([1, 2, 5, 2, 3], 2))
print(target_indices([1, 2, 5, 2, 3], 3))
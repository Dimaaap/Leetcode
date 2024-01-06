def target_indices(nums: list[int], target: int):
    nums = sorted(nums)
    ans = []
    for index, element in enumerate(nums):
        if element == target:
            ans.append(index)
    return ans


print(target_indices([1, 2, 5, 2, 3], 2))
print(target_indices([1, 2, 5, 2, 3], 3))
print(target_indices([1, 2, 5, 2, 3], 5))
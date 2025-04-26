def remove_duplicates(nums: list[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
    such that each unique element appears at most twice. The relative order of the
    elements should be kept the same.
    """
    seen = {}
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen[nums[i]] = 1
            i += 1
        else:
            if seen[nums[i]] != 2:
                seen[nums[i]] += 1
                i += 1
            else:
                nums.pop(i)
    return len(nums)


print(remove_duplicates([1, 1, 1, 2, 2, 3]))
print(remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
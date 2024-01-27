def remove_duplicates(nums: list[int]):
    index = 1
    while index < len(nums):
        if nums[index - 1] == nums[index]:
            nums.remove(nums[index])
        else:
            index += 1
    return len(nums)


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

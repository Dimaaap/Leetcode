def remove_element(nums: list[int], val: int):
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return i


print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
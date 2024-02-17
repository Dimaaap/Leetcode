def move_zeroes(nums: list[int]):
    i = j = 0
    while j < len(nums):
        if nums[j] == 0:
            j += 1
        else:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                i += 1
                j += 1
    return nums


print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0]))
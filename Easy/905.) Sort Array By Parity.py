def sort_array_by_parity(nums: list[int]):
    """
    Given an integer array nums, move all the even integers at the beginning
    of the array followed by all the odd integers.
    Return any array that satisfies this condition.
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] % 2 != 0 and nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] % 2 != 0:
            j -= 1
        elif nums[j] % 2 == 0:
            i += 1
        else:
            i += 1
            j -= 1
    return nums


print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0]))
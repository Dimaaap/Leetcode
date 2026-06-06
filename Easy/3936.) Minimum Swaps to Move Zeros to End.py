def minimum_swaps(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    In one operation, you can choose any two distinct indices i and j and swap nums[i] and nums[j].
    Return an integer denoting the minimum number of operations required to move all 0s to the end of the array.
    """

    i, j = 0, len(nums) - 1
    counter = 0

    while i < j:
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            counter += 1
            i += 1
            j -= 1
            continue
        if nums[i] == 0:
            j -= 1
            continue
        if nums[j] != 0:
            i += 1
            continue
        i += 1
        j -= 1
    return counter


print(minimum_swaps([0, 1, 0, 3, 12]))
print(minimum_swaps([0, 1, 0, 2]))
print(minimum_swaps([1, 2, 0]))
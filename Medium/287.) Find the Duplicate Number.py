def find_duplicate(nums: list[int]):
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            return idx
        nums[idx] = -nums[idx]
    return "What??"


print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))
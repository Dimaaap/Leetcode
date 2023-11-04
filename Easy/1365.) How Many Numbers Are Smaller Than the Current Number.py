def smaller_numbers_than_current(nums: list[int]):
    """
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.
    """
    ans = []
    for i in range(len(nums)):
        less_counter = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                less_counter += 1
        ans.append(less_counter)
    return ans


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))
print(smaller_numbers_than_current([6, 5, 4, 8]))
print(smaller_numbers_than_current([7, 7, 7, 7]))

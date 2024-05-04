def max_operations(nums: list[int]):
    """
    Given an array of integers called nums, you can perform the following operation while nums contains
    at least 2 elements:
    Choose the first two elements of nums and delete them.
    The score of the operation is the sum of the deleted elements.
    Your task is to find the maximum number of operations that can be performed, such that all operations
    have the same score.
    Return the maximum number of operations possible that satisfy the condition mentioned above.
    """
    prev = nums[0] + nums[1]
    count = 1
    i = 2
    while i <= len(nums) - 2:
        if nums[i] + nums[i + 1] == prev:
            count += 1
            i += 2
        else:
            break
    return count


print(max_operations([3, 2, 1, 4, 5]))
print(max_operations([3, 2, 6, 1, 4]))
print(max_operations([1, 1, 1, 1, 1, 1, 2, 1, 1, 2]))
print(max_operations([1, 1, 1, 2, 2, 1, 1, 2, 2, 2]))
def check(nums: list[int]) -> bool:
    """
    Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some
    number of positions (including zero). Otherwise, return false.
    There may be duplicates in the original array.
    Note: An array A rotated by x positions results in an array B of the same length
    such that B[i] == A[(i+x) % A.length] for every valid index i.
    """


    sorted_nums = sorted(nums)
    if sorted_nums == nums:
        return True

    n = len(nums)
    counter = 0
    while counter < n - 1:
        for i in range(1, len(sorted_nums)):
            sorted_nums[i], sorted_nums[i-1] = sorted_nums[i-1], sorted_nums[i]
        if sorted_nums == nums:
            return True
        counter += 1
    return False


print(check([3, 4, 5, 1, 2]))
print(check([2, 1, 3, 4]))
print(check([1, 2, 3]))
def smallest_equal(nums: list[int]):
    """
    Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i],
    or -1 if such index does not exist.
    """
    for index, element in enumerate(nums):
        if index % 10 == element:
            return index
    return -1


print(smallest_equal([0, 1, 2]))
print(smallest_equal([4, 3, 2, 1]))
print(smallest_equal([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
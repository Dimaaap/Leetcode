def max_product(nums: list[int]):
    """
    Given the array of integers nums, you will choose two different indices i and j of that array.
    Return the maximum value of (nums[i]-1)*(nums[j]-1).
    """
    nums.sort()
    product = (nums[-1] - 1) * (nums[-2] - 1)
    return product


print(max_product([3, 4, 5, 2]))
print(max_product([1, 5, 4, 5]))
print(max_product([3, 7]))

def max_product_difference(nums: list[int]):
    sorted_nums = sorted(nums)
    two_smallest = sorted_nums[0] * sorted_nums[1]
    two_largest = sorted_nums[-1] * sorted_nums[-2]
    return two_largest - two_smallest


print(max_product_difference([5, 6, 2, 7, 4]))
print(max_product_difference([4, 2, 5, 9, 7, 4, 8]))

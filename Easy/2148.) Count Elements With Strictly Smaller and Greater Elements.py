def count_elements(nums: list[int]):
    """
    Given an integer array nums, return the number of elements that have both a
    strictly smaller and a strictly greater element appear in nums.
    """
    max_num = max(nums)
    min_num = min(nums)
    counter = 0
    for i in nums:
        if min_num < i < max_num:
            counter += 1
    return counter


print(count_elements([11, 7, 2, 15]))
print(count_elements([-3, 3, 3, 90]))
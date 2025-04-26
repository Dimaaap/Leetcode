def minimum_pair_removal(nums: list[int]) -> int:
    """
    Given an array nums, you can perform the following operation any number of times:
        Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
        Replace the pair with their sum.
        Return the minimum number of operations needed to make the array non-decreasing.
    An array is said to be non-decreasing if each element is greater than or equal to its previous element
    (if it exists).
    """
    counter = 0
    while nums != sorted(nums):
        min_sum = max(nums) * 2
        changed_index = 1
        i = 1
        while i < len(nums):
            nums_sum = nums[i] + nums[i - 1]
            if nums_sum < min_sum:
                min_sum = nums_sum
                changed_index = i
            i += 1
        counter += 1
        nums[changed_index - 1: changed_index + 1] = [min_sum]
    return counter


print(minimum_pair_removal([5, 2, 3, 1]))
print(minimum_pair_removal([1, 2, 2]))

def find_valid_elements(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums.
    An element nums[i] is considered valid if it satisfies at least one of the following conditions:

        It is strictly greater than every element to its left.
        It is strictly greater than every element to its right.
        The first and last elements are always valid.

    Return an array of all valid elements in the same order as they appear in nums.
    """

    if len(nums) == 1:
        return nums

    res = [nums[0]]

    i = 1

    while i < len(nums) - 1:
        if nums[i] > max(nums[:i]) or nums[i] > max(nums[i + 1:]):
            res.append(nums[i])
        i += 1

    res.append(nums[-1])
    return res


print(find_valid_elements([1, 2, 4, 2, 3, 2]))
print(find_valid_elements([5, 5, 5, 5]))
print(find_valid_elements([1]))
print(find_valid_elements([10, 2, 5, 10]))
def min_absolute_difference(nums: list[int]) -> int:
    """
    You are given an integer array nums consisting only of 0, 1, and 2.
    A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.
    Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.
    The absolute difference between indices i and j is defined as abs(i - j).
    """
    min_dif = float("inf")

    for index, num in enumerate(nums):
        for second_index, second_num in enumerate(nums):
            if index != second_index:
                if num == 1 and second_num == 2:
                    abs_dif = abs(index - second_index)
                    min_dif = min(min_dif, abs_dif)
    if min_dif == float("inf"):
        return -1
    return min_dif


print(min_absolute_difference([1, 0, 0, 2, 0, 1]))
print(min_absolute_difference([1, 0, 1, 0]))
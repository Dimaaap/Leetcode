def summary_ranges(nums: list[int]):
    """
    You are given a sorted unique integer array nums.
    A range [a,b] is the set of all integers
    from a to b (inclusive).
    Return the smallest sorted list of ranges that
    cover all the numbers in the array exactly.
    That is, each element of nums is covered by exactly
    one of the ranges, and there is no integer x such that
    x is in one of the ranges but not in nums.
    """
    temp_list = []
    result_list = []
    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            temp_list.extend([str(nums[i]), str(nums[i + 1])])
        else:
            result_list.append(temp_list)
            temp_list = []
    result_list.append(temp_list)
    return nums


print(summary_ranges([0, 1, 2, 4, 5, 7]))
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))

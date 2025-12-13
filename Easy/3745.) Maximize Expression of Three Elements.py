def maximize_expression_of_three(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    Choose three elements a, b, and c from nums at distinct indices such that the value of
    the expression a + b - c is maximized.
    Return an integer denoting the maximum possible value of this expression.
    """
    sorted_nums = sorted(nums)
    max1, max2 = sorted_nums[-2:]
    min_val = sorted_nums[0]
    return max1 + max2 - min_val


print(maximize_expression_of_three([1, 4, 2, 5]))
print(maximize_expression_of_three([-2, 0, 5, -2, 4]))
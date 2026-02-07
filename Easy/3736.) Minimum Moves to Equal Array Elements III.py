def min_moves(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    In one move, you may increase the value of any single element nums[i] by 1.
    Return the minimum total number of moves required so that all elements in nums become equal.
    """

    max_el = max(nums)
    res = 0

    for num in nums:
        res += max_el - num
    return res


print(min_moves([2, 1, 3]))
print(min_moves([4, 4, 5]))
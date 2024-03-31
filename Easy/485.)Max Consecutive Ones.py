def find_max_consecutive_ones(nums: list[int]):
    """
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    """
    ans = 0
    max_ans = ans
    for num in nums:
        if num == 1:
            ans += 1
        else:
            max_ans = max(max_ans, ans)
            ans = 0
    return max(max_ans, ans)


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
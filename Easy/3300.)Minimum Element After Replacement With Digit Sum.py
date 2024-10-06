def min_element(nums: list[int]) -> int:
    """
    You are given an integer array nums.

    You replace each element in nums with the sum of its digits.

    Return the minimum element in nums after all replacements.
    """
    nums_str = [str(num) for num in nums]
    ans = max(nums)
    for num in nums_str:
        digit_sum = 0
        for i in num:
            digit_sum += int(i)
        ans = min(ans, digit_sum)
    return ans


print(min_element([10, 12, 13, 14]))
print(min_element([1, 2, 3, 4]))
print(min_element([999, 19, 199]))
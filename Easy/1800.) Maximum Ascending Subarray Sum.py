def max_ascending_sum(nums: list[int]):
    """
    Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
    A subarray is defined as a contiguous sequence of numbers in an array.
    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1.
    Note that a subarray of size 1 is ascending.
    """
    if len(nums) == 1:
        return nums[0]
    stack = []
    ans = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            stack.append(nums[i])
        else:
            stack.append(nums[i])
            ans = max(sum(stack), ans)
            stack = []
    if stack and nums[-1] > stack[-1]:
        stack.append(nums[-1])
        ans = max(sum(stack), ans)
    return ans


print(max_ascending_sum([10, 20, 30, 5, 10, 50]))
print(max_ascending_sum([10, 20, 30, 40, 50]))
print(max_ascending_sum([12, 17, 15, 13, 10, 11, 12]))
print(max_ascending_sum([100, 10, 1]))
print(max_ascending_sum([6]))

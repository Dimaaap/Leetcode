def triangular_sum(nums: list[int]):
    """
    You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).
    The triangular sum of nums is the value of the only element present in nums after the following process terminates:

    Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array
    newNums of length n - 1.
    For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10,
     where % denotes modulo operator.
    Replace the array nums with newNums.
    Repeat the entire process starting from step 1.
    Return the triangular sum of nums.
    """
    new_ans = []
    while len(nums) != 1:
        for i in range(len(nums)-1):
            res = (nums[i] + nums[i+1]) % 10
            new_ans.append(res)
        nums = new_ans
        new_ans = []
    return nums[0]


print(triangular_sum([1, 2, 3, 4, 5]))
print(triangular_sum([5]))



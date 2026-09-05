def get_maximum_generated(n: int) -> int:
    """
    You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
        nums[0] = 0
        nums[1] = 1
        nums[2 * i] = nums[i] when 2 <= 2 * i <= n
        nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
    Return the maximum integer in the array nums.
    """

    if n == 0:
        return 0

    res = [0, 1] + [0] * (n - 1)
    i = 1
    while i < (len(res) // 2) + 1:
        if 2 * i < len(res):
            res[2 * i] = res[i]
        if 2 * i + 1 < len(res):
            res[2 * i + 1] = res[i] + res[i + 1]
        i += 1
    return max(res)


print(get_maximum_generated(7))
print(get_maximum_generated(2))
print(get_maximum_generated(3))
print(get_maximum_generated(0))
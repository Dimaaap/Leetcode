def min_operations(nums: list[int]) -> int:
    """
    You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some
    (possibly zero) operations on the array so that all elements become 0.
    In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the
    minimum non-negative integer in that subarray to 0.
    Return the minimum number of operations required to make all elements in the array 0.
    """
    stack = []
    res = 0
    for n in nums:
        while stack and stack[-1] > n:
            stack.pop()
        if n == 0:
            continue
        if not stack or stack[-1] < n:
            res += 1
            stack.append(n)
    return res


print(min_operations([0, 2]))
print(min_operations([3, 1, 2, 1]))
print(min_operations([1, 2, 1, 2, 1, 2]))
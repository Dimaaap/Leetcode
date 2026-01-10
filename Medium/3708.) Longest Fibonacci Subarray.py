def longest_subarray(nums: list[int]) -> int:
    """
    You are given an array of positive integers nums.
    A Fibonacci array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding
    terms.
    Return the length of the longest Fibonacci subarray in nums.
    Note: Subarrays of length 1 or 2 are always Fibonacci.
    """
    i = 0
    max_length = 0
    found = False
    window = []
    while i < len(nums) - 2:
        if not found:
            window = [nums[i], nums[i + 1]]
        is_fib_subarray = nums[i] + nums[i + 1] == nums[i + 2]
        if is_fib_subarray:
            window.append(nums[i + 2])
            found = True
        else:
            max_length = max(max_length, len(window))
            found = False
        i += 1
    if window:
        max_length = max(max_length, len(window))
    return max_length


print(longest_subarray([1, 1, 1, 1, 2, 3, 5, 1]))
print(longest_subarray([5, 2, 7, 9, 16]))
print(longest_subarray([1000000000, 1000000000, 1000000000]))
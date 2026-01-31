def centered_subarrays(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    A subarray of nums is called centered if the sum of its elements is equal to at least one element within
    that same subarray.
    Return the number of centered subarrays of nums.
    """

    counter = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
           subarray = nums[i:j + 1]
           subarray_sum = sum(subarray)
           if subarray_sum in subarray:
               counter += 1
    return counter


print(centered_subarrays([-1, 1, 0]))
print(centered_subarrays([2, -3]))
def count_majority_subarrays(nums: list[int], target: int) -> int:
    """
    You are given an integer array nums and an integer target.
    Return the number of subarrays of nums in which target is the majority element.
    The majority element of a subarray is the element that appears strictly more than half of the
    times in that subarray.
    """
    res = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            target_count = subarray.count(target)
            if target_count * 2 > len(subarray):
                res += 1
    return res


print(count_majority_subarrays([1, 2, 2, 3], 2))
print(count_majority_subarrays([1, 1, 1, 1], 1))
print(count_majority_subarrays([1, 2, 3], 4))
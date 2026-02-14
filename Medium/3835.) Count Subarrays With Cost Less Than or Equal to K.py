def count_subarrays(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums, and an integer k. For any subarray nums[l..r], define its cost as:
    cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1)
    Return an integer denoting the number of subarrays of nums whose cost is less than or equal to k.
    """
    counter = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]

            cost = (max(subarray) - min(subarray)) * (j - i + 1)
            if cost <= k:
                counter += 1

    return counter


print(count_subarrays([1, 3, 2], 4))
print(count_subarrays([5, 5, 5, 5], 0))
print(count_subarrays([1, 2, 3], 0))

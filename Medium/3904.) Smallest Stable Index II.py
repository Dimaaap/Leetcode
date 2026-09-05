def first_stable_index(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums of length n and an integer k.
    For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

    In other words:
        max(nums[0..i]) is the largest value among the elements from index 0 to index i.
        min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

    An index i is called stable if its instability score is less than or equal to k.
    Return the smallest stable index. If no such index exists, return -1.
    """

    n = len(nums)

    right_min = [0] * n
    right_min[-1] = nums[-1]

    for i in range(n - 2, -1, -1):
        right_min[i] = min(nums[i], right_min[i + 1])

    left_max = 0

    for i in range(n):
        left_max = max(left_max, nums[i])

        if left_max - right_min[i] <= k:
            return i
    return -1


print(first_stable_index([5, 0, 1, 4], 3))
print(first_stable_index([3, 2, 1], 1))
print(first_stable_index([0], 0))
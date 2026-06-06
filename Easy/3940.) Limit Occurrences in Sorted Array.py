from collections import defaultdict


def limit_occurrences(nums: list[int], k: int) -> list[int]:
    """
    You are given a sorted integer array nums and an integer k.
    Return an array such that each distinct element appears at most k times, while preserving the
    relative order of the elements in nums.
    Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.
    """

    counter = defaultdict(int)
    res = []

    for num in nums:
        if counter[num] < k:
            counter[num] += 1
    for nums in counter:
        res.extend([nums] * counter[nums])
    return res


print(limit_occurrences([1, 1, 1, 2, 2, 3], 2))
print(limit_occurrences([1, 2, 3], 1))
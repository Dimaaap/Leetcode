from collections import defaultdict


def min_distinct_freq_pair(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums.
    Consider all pairs of distinct values x and y from nums such that:
        x < y
        x and y have different frequencies in nums.
    Among all such pairs:
    Choose the pair with the smallest possible value of x.
    If multiple pairs have the same x, choose the one with the smallest possible value of y.
    Return an integer array [x, y]. If no valid pair exists, return [-1, -1].
    """

    nums = sorted(nums)
    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1

    min_el = min(nums)
    min_freq = counter[min_el]
    another_el = None

    for key, value in counter.items():
        if key != min_el and value != min_freq:
            another_el = key
            break
    if another_el and min_el:
        return [min_el, another_el]
    return [-1, -1]


print(min_distinct_freq_pair([1, 1, 2, 2, 3, 4]))
print(min_distinct_freq_pair([1, 5]))
print(min_distinct_freq_pair([7]))
print(min_distinct_freq_pair([1, 1, 4, 3]))
from collections import Counter, defaultdict


def first_unique_freq(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    Return an integer denoting the first element (scanning from left to right) in nums whose frequency is unique.
    That is, no other integer appears the same number of times in nums. If there is no such element, return -1.
    """

    counter = Counter(nums)
    counter = tuple(counter.items())
    res = defaultdict(list)

    for num, freq in counter:
        res[freq].append(num)

    for freq, nums in dict(res).items():
        if len(nums) == 1:
            return nums[0]
    return -1


print(first_unique_freq([20, 10, 30, 30]))
print(first_unique_freq([20, 20, 10, 30, 30, 30]))
print(first_unique_freq([10, 10, 20, 20]))

def max_k_distinct(nums: list[int], k: int) -> list[int]:
    """
    You are given a positive integer array nums and an integer k.
    Choose at most k elements from nums so that their sum is maximized. However, the chosen numbers must be distinct.
    Return an array containing the chosen numbers in strictly descending order.
    """

    nums = list(set(nums))
    nums = sorted(nums)[::-1]
    res = nums[:k]

    return res


print(max_k_distinct([84, 93, 100, 77, 90], 3))
print(max_k_distinct([84, 93, 100, 77, 93], 3))
print(max_k_distinct([1, 1, 1, 2, 2, 2], 6))
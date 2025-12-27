def sum_divisible_by_k(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k.
    Return an integer denoting the sum of all elements in nums whose frequency is divisible by k,
    or 0 if there are no such elements.
    Note: An element is included in the sum exactly as many times as it appears in the array if its total
    frequency is divisible by k.

    """
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    res = 0
    for num, frequency in freq.items():
        if frequency % k == 0:
            res += (num * frequency)
    return res


print(sum_divisible_by_k([1, 2, 2, 3, 3, 3, 3, 4], 2))
print(sum_divisible_by_k([1, 2, 3, 4, 5], 2))
print(sum_divisible_by_k([4, 4, 4, 1, 2, 3], 3))
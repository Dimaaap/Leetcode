def missing_multiple(nums: list[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.
    A multiple of k is any positive integer divisible by k.
    """

    start = k
    while True:
        if start not in nums:
            return start
        else:
            start += k


print(missing_multiple([8, 2, 3, 4, 6], 2))
print(missing_multiple([1, 4, 7, 10, 15], 5))
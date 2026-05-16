def count_opposite_parity(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums of length n.
    The score of an index i is defined as the number of indices j such that:
        i < j < n, and
        nums[i] and nums[j] have different parity (one is even and the other is odd).
    Return an integer array answer of length n, where answer[i] is the score of index i.
    """

    def count_odds(digits: list[int]) -> int:
        counter = 0

        for digit in digits:
            if digit % 2 == 0:
                counter += 1
        return counter


    res = []
    i, j = 0, len(nums) - 1

    while i < len(nums):
        if nums[i] % 2 != 0:
            res.append(count_odds(nums[i+1:]))
        else:
            res.append(len(nums[i + 1:]) - count_odds(nums[i + 1:]))
        i += 1

    return res


print(count_opposite_parity([1, 2, 3, 4]))
print(count_opposite_parity([1]))
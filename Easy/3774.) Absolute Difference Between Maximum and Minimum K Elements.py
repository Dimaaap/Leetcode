def abs_difference(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k.
    Find the absolute difference between:
    the sum of the k largest elements in the array; and
    the sum of the k smallest elements in the array.
    Return an integer denoting this difference.
    """
    sorted_nums = sorted(nums)
    k_max = sorted_nums[-k:]
    k_min = sorted_nums[:k]
    max_sum, min_sum = sum(k_max), sum(k_min)
    return abs(max_sum - min_sum)


print(abs_difference([5, 2, 2, 4], 2))
print(abs_difference([100], 1))
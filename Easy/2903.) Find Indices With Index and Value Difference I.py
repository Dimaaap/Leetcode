def find_indices(nums: list[int], index_difference: int, value_difference: int):
    """
    You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer
    valueDifference.
    Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:
        abs(i - j) >= indexDifference, and
        abs(nums[i] - nums[j]) >= valueDifference
    Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1]
    otherwise. If there are multiple choices for the two indices, return any of them.
    Note: i and j may be equal.
    """
    for index, element in enumerate(nums):
        for j, el in enumerate(nums):
            if abs(index - j) >= index_difference and abs(element - el) >= value_difference:
                return [index, j]
    return [-1, -1]


print(find_indices([5, 1, 4, 1], 2, 4))
print(find_indices([2, 1], 0, 0))
print(find_indices([1, 2, 3], 2, 4))
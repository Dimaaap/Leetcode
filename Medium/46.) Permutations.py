from itertools import permutations


def permute(nums: list[int]) -> list[list[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    """
    all_permutations = permutations(nums)
    return [list(perm) for perm in all_permutations]


print(permute([1, 2, 3]))



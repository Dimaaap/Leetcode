from collections import defaultdict


def count_special_integers(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    An integer x is called special if:
        x appears exactly three times in nums.
        All three occurrences of x are equally spaced in nums. In other words, if all occurrences of
        x are at indices i1 < i2 < i3, then i2 - i1 = i3 - i2.
    Return the number of distinct special integers in nums.
    """

    nums_map = defaultdict(list)

    for index, num in enumerate(nums):
        nums_map[num].append(index)

    counter = 0

    for key, value in nums_map.items():
        if len(value) != 3:
            continue
        if value[2] - value[1] == value[1] - value[0]:
            counter += 1
    return counter

print(count_special_integers([1, 8, 1, 5, 1, 5, 8, 5]))
print(count_special_integers([8, 8, 8, 8]))
print(count_special_integers([8, 6, 6, 8, 8]))
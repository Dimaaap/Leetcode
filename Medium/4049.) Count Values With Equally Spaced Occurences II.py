from collections import defaultdict


def count_special_integers(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    An integer x is called special if:
        x appears at least three times in nums.
        All occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at
        indices i1 < i2 < ... < im, then i2 - i1 = i3 - i2 = ... = im - im-1.
    Return the number of distinct special integers in nums.
    """

    nums_map = defaultdict(list)

    for index, num in enumerate(nums):
        nums_map[num].append(index)

    res = 0

    for key, value in nums_map.items():
        if len(value) < 3:
            continue
        diff = value[1] - value[0]
        i = len(value) - 1

        while i > 1:
            if value[i] - value[i - 1] != diff:
                break
            i -= 1
        else:
            res += 1
    return res

print(count_special_integers([1, 8, 1, 5, 1, 5, 8, 5]))
print(count_special_integers([8, 8, 8, 8]))
print(count_special_integers([8, 6, 6, 8, 8]))

from collections import defaultdict


def count_nice_pairs(nums: list[int]) -> int:
    """
    You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the
    non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
    satisfies all of the following conditions:

        0 <= i < j < nums.length
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
    """
    def rev(num: int) -> int:
        str_num = str(num)[::-1]
        return int(str_num)

    MOD = 10 ** 9 + 7
    values_map = defaultdict(int)

    for i in range(len(nums)):
        values_map[nums[i] - rev(nums[i])] += 1

    counter = 0
    for value in values_map.values():
        pairs = value * (value - 1) // 2
        counter = (counter + pairs) % MOD
    return counter


print(count_nice_pairs([42, 11, 1, 97]))
print(count_nice_pairs([13, 10, 35, 24, 76]))
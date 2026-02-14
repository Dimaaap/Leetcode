from collections import deque


def merge_adjacent(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums.
    You must repeatedly apply the following merge operation until no more changes can be made
    If any two adjacent elements are equal, choose the leftmost such adjacent pair in the current array and replace \
    them with a single element equal to their sum.

    After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no
    more changes can be made.
    Return the final array after all possible merge operations.
    """
    stack = deque()
    i = 0

    while i < len(nums):
        el = nums[i]

        if not stack or el != stack[-1]:
            stack.append(el)
            i += 1
        else:
            new_num = nums[i] * 2
            _ = stack.pop()
            stack.append(new_num)
            nums[i -1: i + 1] = [new_num]
            i = 0
            stack = deque()
    return list(stack)


print(merge_adjacent([3, 1, 1, 2]))
print(merge_adjacent([2, 2, 4]))
print(merge_adjacent([3, 7, 5]))
print(merge_adjacent([2, 1, 1, 2]))


def maximum_count(nums: list[int]):
    """
    Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers
     and the number of negative integers.
    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg,
     then return the maximum of pos and neg.
    Note that 0 is neither positive nor negative.
    """
    pos_counter = neg_counter = 0
    for i in nums:
        if i < 0:
            neg_counter += 1
        elif i > 0:
            pos_counter += 1
    return max(neg_counter, pos_counter)


print(maximum_count([-2, -1, -1, 1, 2, 3]))
print(maximum_count([-3, -2, -1, 0, 0, 1, 2]))
print(maximum_count([5, 20, 66, 1314]))
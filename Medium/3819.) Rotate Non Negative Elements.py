def rotate_elements(nums: list[int], k: int) -> list[int]:
    """
    You are given an integer array nums and an integer k.
    Rotate only the non-negative elements of the array to the left by k positions, in a cyclic manner.
    All negative elements must stay in their original positions and must not move.
    After rotation, place the non-negative elements back into the array in the new order, filling only the positions
    that originally contained non-negative values and skipping all negative positions.
    Return the resulting array.
    """

    pos_elements = []
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            pos_elements.append(nums[i])
            nums[i] = "_"
        i += 1

    if len(pos_elements) == 0:
        return nums
    k = k % len(pos_elements)

    if k == 0:
        pos_elements = pos_elements
    else:
        pos_elements = pos_elements[k:] + pos_elements[:k]

    j = 0
    for i in range(len(nums)):
        if nums[i] == "_":
            nums[i] = pos_elements[j]
            j += 1
    return nums


print(rotate_elements([1, -2, 3, -4], 3))
print(rotate_elements([-3, -2, 7], 1))
print(rotate_elements([5, 4, -9, 6], 2))

def rotate(nums: list[int], k: int) -> None:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """
    n = len(nums)
    rotated = [0] * n
    for i in range(n):
        insert_position = (i + k) % n
        rotated[insert_position] = nums[i]
    nums = [i for i in rotated]
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))
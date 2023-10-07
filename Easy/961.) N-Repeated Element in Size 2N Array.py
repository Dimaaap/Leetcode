def repeated_n_times(nums: list[int]):
    """
    You are given an integer array nums with the following properties:
    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.
    Return the element that is repeated n times.
    """
    visited = set()
    for num in nums:
        if num in visited:
            return num
        else:
            visited.add(num)


print(repeated_n_times([1, 2, 3, 3]))
print(repeated_n_times([2, 1, 2, 5, 3, 2]))
print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))

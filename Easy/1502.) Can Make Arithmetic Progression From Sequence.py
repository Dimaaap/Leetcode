def can_make_arithmetic_progression(arr: list[int]):
    """
    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
    Otherwise, return false.
    """
    arr.sort()
    diff_set = set()
    for i in range(len(arr) - 1):
        diff_set.add(arr[i + 1] - arr[i])
    return len(diff_set) == 1


print(can_make_arithmetic_progression([3, 5, 1]))
print(can_make_arithmetic_progression([1, 2, 4]))

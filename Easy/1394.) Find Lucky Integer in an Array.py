def find_lucky(arr: list[int]):
    """
    Given an array of integers arr, a lucky integer is an integer that has a frequency
    in the array equal to its value.
    Return the largest lucky integer in the array. If there is no lucky integer return -1.
    """
    ans = -1
    for i in arr:
        if arr.count(i) == i:
            ans = max(ans, i)
    return ans


print(find_lucky([2, 2, 3, 4]))
print(find_lucky([1, 2, 2, 3, 3, 3]))
print(find_lucky([2, 2, 2, 3, 3]))
def three_consecutive_odds(arr: list[int]):
    """
    Given an integer array arr, return true if there are three consecutive odd numbers in the array.
    Otherwise, return false.
    """
    sliding = []
    for i in arr:
        if i % 2 != 0:
            sliding.append(i)
        else:
            sliding = []
        if len(sliding) == 3:
            return True
    return False


print(three_consecutive_odds([2, 6, 4, 1]))
print(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
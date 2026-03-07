def check_if_exist(arr: list[int]):
    """
    Given an array arr of integers, check if there exist two indices i and j such that :
        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]
    """
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i / 2)
        seen.add(i * 2)
    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([3, 1, 7, 11]))
print(check_if_exist([7, 1, 14, 11]))
def replace_elements(arr: list[int]) -> list[int]:
    """
    Given an array arr, replace every element in that array with the greatest element among the elements to
    its right, and replace the last element with -1.
    After doing so, return the array.
    """

    max_right = -1

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))
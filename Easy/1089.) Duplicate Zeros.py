def duplicate_zeros(arr: list[int]):
    i = 0
    start_len = len(arr)
    while i < len(arr) - 1:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            i += 2
        else:
            i += 1
    return arr[:start_len]


print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([1, 2, 3]))

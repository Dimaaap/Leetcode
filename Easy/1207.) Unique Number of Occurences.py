def unique_occurrences(arr: list[int]):
    occur_dict = {}
    for i in arr:
        if i not in occur_dict:
            occur_dict[i] = arr.count(i)
    return len(set(occur_dict.values())) == len(occur_dict.values())


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
print(unique_occurrences([1, 2]))
print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
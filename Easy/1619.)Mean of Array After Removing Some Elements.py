def trim_mean(arr: list[int]):
    """
    Given an integer array arr, return the mean of the remaining integers
     after removing the smallest 5% and the largest 5% of the elements.
    """
    count_elements_to_delete = len(arr) // 10
    delete_min_elements = count_elements_to_delete // 2
    new_list = sorted(arr)[delete_min_elements: len(arr) - delete_min_elements]
    return sum(new_list) / len(new_list)


print(trim_mean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
print(trim_mean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]))
print(trim_mean(
    [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2,
     3, 4]))

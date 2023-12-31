def trim_mean(arr: list[int]):
    """
    Given an integer array arr, return the mean of the remaining integers after
    removing the smallest 5% and the largest 5% of the elements.
    Answers within 10-5 of the actual answer will be considered accepted.
    """
    n = len(arr)
    per_cents = int(n * 5 / 100)
    sorted_array = sorted(arr)[per_cents:n - per_cents]
    return round(sum(sorted_array) / len(sorted_array), 5)


print(trim_mean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
print(trim_mean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]))
print(trim_mean(
    [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2,
     3, 4]))

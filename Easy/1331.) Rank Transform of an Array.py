def array_rank_transform(arr: list[int]) -> list[int]:
    """
    Given an array of integers arr, replace each element with its rank.
    The rank represents how large the element is. The rank has the following rules:
        Rank is an integer starting from 1.
        The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
        Rank should be as small as possible.
    """

    sorted_unique = sorted(set(arr))
    rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
    return [rank_dict[num] for num in arr]


print(array_rank_transform([40, 10, 20, 30]))
print(array_rank_transform([100, 100, 100]))
print(array_rank_transform([37,12,28,9,100,56,80,5,12]))
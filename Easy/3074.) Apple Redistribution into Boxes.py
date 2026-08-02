def minimum_boxes(apple: list[int], capacity: list[int]) -> int:
    """
    You are given an array apple of size n and an array capacity of size m.
    There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box
    has a capacity of capacity[i] apples.
    Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
    Note that, apples from the same pack can be distributed into different boxes.
    """

    apples_count = sum(apple)

    capacity = sorted(capacity)[::-1]
    current_capacity = 0

    for i, box in enumerate(capacity, 1):
        current_capacity += box
        if current_capacity >= apples_count:
            return i
    return current_capacity

print(minimum_boxes([1, 3, 2], [4, 3, 1, 5, 2]))
print(minimum_boxes([5, 5, 5], [2, 4, 2, 7]))
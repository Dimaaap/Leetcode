def minimum_boxes(apple: list[int], capacity: list[int]):
    """
    You are given an array apple of size n and an array capacity of size m.

    There are n packs where the ith pack contains apple[i] apples. There are m boxes as well,
    and the ith box has a capacity of capacity[i] apples.

    Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

    Note that, apples from the same pack can be distributed into different boxes.
    """
    apples_count = sum(apple)
    sum_boxes = 0
    counter = 0
    capacity = sorted(capacity)
    for box in capacity[::-1]:
        if sum_boxes >= apples_count:
            break
        sum_boxes += box
        counter += 1
    return counter


print(minimum_boxes([1, 3, 2], [4, 3, 1, 5, 2]))
print(minimum_boxes([5, 5, 5], [2, 4, 2, 7]))
def minimum_index(capacity: list[int], item_size: int) -> int:
    """
    You are given an integer array capacity, where capacity[i] represents the capacity of the ith
    box, and an integer itemSize representing the size of an item.
    The ith box can store the item if capacity[i] >= itemSize.
    Return an integer denoting the index of the box with the minimum capacity that can store
    the item. If multiple such boxes exist, return the smallest index.
    If no box can store the item, return -1.
    """
    min_el, min_index = float("inf"), float("inf")

    for index, el in enumerate(capacity):
        if el >= item_size:
            if el < min_el:
                min_index = index
                min_el = el
    if min_index != float("inf"):
        return min_index
    return -1


print(minimum_index([1, 5, 3, 7], 3))
print(minimum_index([3, 5, 4, 3], 2))
print(minimum_index([4], 5))
print(minimum_index([7, 7], 3))
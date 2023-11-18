def pick_gifts(gifts: list[int], k: int):
    """
    You are given an integer array gifts denoting the number of gifts in various piles. Every second,
    you do the following:
        Choose the pile with the maximum number of gifts.
        If there is more than one pile with the maximum number of gifts, choose any.
        Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
    Return the number of gifts remaining after k seconds.
    """
    a = 0
    while a < k:
        gifts.sort()
        max_el = int(gifts[-1] ** 0.5)
        gifts[-1] = max_el
        a += 1
    return sum(gifts)


print(pick_gifts([25, 64, 9, 4, 100], 4))
print(pick_gifts([1, 1, 1, 1], 4))

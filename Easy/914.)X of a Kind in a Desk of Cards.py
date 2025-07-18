def has_group_size_x(deck: list[int]) -> bool:
    """
    You are given an integer array deck where deck[i] represents the number written on the ith card.

    Partition the cards into one or more groups such that:

    Each group has exactly x cards where x > 1, and
    All the cards in one group have the same integer written on them.
    Return true if such partition is possible, or false otherwise.
    """
    if len(deck) < 2:
        return False

    count = [deck.count(i) for i in set(deck)]
    result = count[0]

    for i in count[1:]:
        result = gcd(result, i)

    return result >= 2


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a




print(has_group_size_x([1, 2, 3, 4, 4, 3, 2, 1])) # -> True
print(has_group_size_x([1, 1, 1, 2, 2, 2, 3, 3])) # -> False
print(has_group_size_x([1])) # -> False
print(has_group_size_x([1, 1, 2, 2, 2, 2])) # -> True
print(has_group_size_x([1, 1, 1, 1, 2, 2, 2, 2, 2, 2])) # -> True
print(has_group_size_x([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3])) # -> False
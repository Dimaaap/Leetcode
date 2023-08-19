def has_group_size_x(deck: list[int]):
    x = deck.count(deck[0])
    for i in deck[1:]:
        if deck.count(i) != x or x <= 1:
            return False
    return True


print(has_group_size_x([1, 2, 3, 4, 4, 3, 2, 1]))
print(has_group_size_x([1, 1, 1, 2, 2, 2, 3, 3]))
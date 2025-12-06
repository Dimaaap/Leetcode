def recover_order(order: list[int], friends: list[int]) -> list[int]:
    res = []
    friends = set(friends)
    for o in order:
        if o in friends:
            res.append(o)
    return res


print(recover_order([3, 1, 2, 5, 4], [1, 3, 4]))
print(recover_order([1, 4, 5, 3, 2], [2, 5]))
def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    """
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is
    to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it. Each key has a number on it,
    which room it unlocks, and you can take all of them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
    return true if you can visit all the rooms, or false otherwise.
    """
    keys = [rooms[0]]
    rooms[0] = True
    while keys:
        key = keys.pop()
        for k in key:
            if not isinstance(rooms[k], bool):
                keys.append(rooms[k])
                rooms[k] = True
    return all(i is True for i in rooms)


print(can_visit_all_rooms([[1], [2], [3], []]))
print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))


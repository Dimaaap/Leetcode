from collections import deque


def rearrange_string(s: str, x: str, y: str) -> str:
    s = list(s)
    res = deque()

    for char in s[::-1]:
        if char == y:
            res.appendleft(char)
        elif char == x:
            res.append(char)
        else:
            res.appendleft(char)
    new_list = "".join(list(res))

    return new_list


print(rearrange_string("aabc", "a", "c"))
print(rearrange_string("dcab", "d", "b"))
print(rearrange_string("axe", "o", "x"))


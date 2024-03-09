def pass_the_pillow(n: int, time: int):
    """
    There are n people standing in a line labeled from 1 to n.
    The first person in the line is holding a pillow initially. Every second, the person holding the pillow
    passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction
    changes, and people continue passing the pillow in the opposite direction.
    For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n -
    2th person and so on.
    Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.
    """
    index = 1
    direction = 1
    while time > 0:
        if direction == 1:
            index += 1
            if index == n:
                direction *= -1
        else:
            index -= 1
            if index == 1:
                direction *= -1
        time -= 1
    return index


print(pass_the_pillow(4, 5))
print(pass_the_pillow(3, 2))
def number_of_child(n: int, k: int) -> int:
    """
    You are given two positive integers n and k. There are n children numbered from 0 to n - 1 standing in a
    queue in order from left to right.
    Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction.
    After each second, the child holding the ball passes it to the child next to them. Once the ball reaches either
    end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.

    Return the number of the child who receives the ball after k seconds.
    :param n:
    :param k:
    :return:
    """
    on_right = True
    pointer = 0
    while k:
        if pointer == n - 1:
            on_right = False
        elif pointer == 0:
            on_right = True
        if on_right:
            pointer += 1
        else:
            pointer -= 1
        k -= 1
    return pointer


print(number_of_child(3, 5))
print(number_of_child(5, 6))
print(number_of_child(4, 2))



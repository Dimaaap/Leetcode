def count_symmetric_integers(low: int, high: int):
    """
    You are given two positive integers low and high.

    An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal
    to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

    Return the number of symmetric integers in the range [low, high].
    """
    counter = 0
    for i in range(low, high + 1):
        if is_symmetric(i):
            counter += 1
    return counter


def is_symmetric(n: int):
    n = str(n)
    if len(n) % 2 == 0:
        middle = len(n) // 2
        list_number = [int(i) for i in n]
        return sum(list_number[:middle]) == sum(list_number[middle:])
    else:
        return False


print(count_symmetric_integers(1, 100))
print(count_symmetric_integers(1200, 1230))
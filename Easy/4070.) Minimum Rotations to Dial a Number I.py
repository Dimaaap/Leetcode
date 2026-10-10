def min_rotations(s: str) -> int:
    """
    You are given a string s of length 10 consisting of digits.
    The dial contains the digits 0 through 9 in order and is circular, so 0 and 9 are adjacent.
    The pointer initially points to 0.
    To dial each digit of s in order, rotate the pointer until it points to that digit. Each rotation moves
    the pointer to an adjacent digit, and you may rotate in either direction. Dialing a digit that the pointer already points to requires no rotations.
    Return the minimum total number of rotations needed to dial every digit of s.
    """

    steps = 0
    dial = tuple(range(0, 10))
    current_pos = 0

    for index, char in enumerate(s):
        char = int(char)
        diff = abs(current_pos - char)
        step = min(diff, 10 - diff)
        steps += step
        current_pos = dial.index(char)
    return steps


print(min_rotations("0192837465"))
print(min_rotations("1200210200"))
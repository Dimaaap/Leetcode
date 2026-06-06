def is_adjacent_diff_at_most_two(s: str) -> bool:
    """
    You are given a string s consisting of digits.
    Return true if the absolute difference between every pair of adjacent digits is at most 2, otherwise return false.
    The absolute difference between a and b is defined as abs(a - b).
    """

    for i in range(len(s) - 1):
        first_digit, second_digit = int(s[i]), int(s[i + 1])
        if abs(first_digit - second_digit) > 2:
            return False

    return True


print(is_adjacent_diff_at_most_two("132"))
print(is_adjacent_diff_at_most_two("129"))

def rotate_string(s: str, goal: str) -> bool:
    """
    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the rightmost position.
    For example, if s = "abcde", then it will be "bcdea" after one shift.
    """

    s = list(s)
    goal = list(goal)

    shifts = len(s)
    counter = 0
    while counter < shifts:

        if s == goal:
            return True

        for i in range(1, len(s)):
            s[i], s[i - 1] = s[i - 1], s[i]
        counter += 1
    return False


print(rotate_string("abcde", "cdeab"))
print(rotate_string("abcde", "abced"))
print(rotate_string("dawhwh", "hdawhw"))

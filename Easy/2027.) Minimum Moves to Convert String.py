def minimum_moves(s: str):
    """
    You are given a string s consisting of n characters which are either 'X' or 'O'.
    A move is defined as selecting three consecutive characters of s and converting them to 'O'.
    Note that if a move is applied to the character 'O', it will stay the same.
    Return the minimum number of moves required so that all the characters of s are converted to 'O'.

    """
    ans = i = 0
    while i < len(s):
        if s[i] == "X":
            ans += 1
            i += 3
        else:
           i += 1
    return ans


print(minimum_moves("XXX"))
print(minimum_moves("XX0X"))
print(minimum_moves("0000"))
print(minimum_moves("0X0X"))

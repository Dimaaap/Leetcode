def string_sequence(target: str) -> list[str]:
    """
    You are given a string target.

    Alice is going to type target on her computer using a special keyboard that has only two keys:

        Key 1 appends the character "a" to the string on the screen.
        Key 2 changes the last character of the string on the screen to its next character in the English alphabet.
        For example, "c" changes to "d" and "z" changes to "a".

    Note that initially there is an empty string "" on the screen, so she can only press key 1.

    Return a list of all strings that appear on the screen as Alice types target, in the order they appear,
    using the minimum key presses.
    """
    ans = ["a"]
    i = j = 0
    while ans[-1] != target:
        if ans[-1][j] == target[i]:
            ans.append(ans[-1][:j+1] + "a")
            j += 1
            i += 1
        else:
            ans.append(ans[-1][:j] + chr(ord(ans[-1][j]) + 1))
    return ans


print(string_sequence("abc"))
print(string_sequence("he"))


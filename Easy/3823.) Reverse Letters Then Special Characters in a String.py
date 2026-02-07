import string


def reverse_by_type(s: str) -> str:
    """
    You are given a string s consisting of lowercase English letters and special characters.
    Your task is to perform these in order:
        Reverse the lowercase letters and place them back into the positions
        originally occupied by letters.
        Reverse the special characters and place them back into the positions originally
        occupied by special characters.

    Return the resulting string after performing the reversals.
    """
    letters = string.ascii_lowercase
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] in letters and s[j] in letters:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in letters:
            j -= 1
        elif s[j] in letters:
            i += 1
        else:
            i += 1
            j -= 1

    k, n = 0, len(s) - 1
    while k < n:
        if s[k] not in letters and s[n] not in letters:
            s[k], s[n] = s[n], s[k]
            k += 1
            n -= 1
        elif s[k] not in letters:
            n -= 1
        elif s[n] not in letters:
            k += 1
        else:
            k += 1
            n -= 1
    return "".join(s)


print(reverse_by_type(")ebc#da@f("))
print(reverse_by_type("z"))
print(reverse_by_type("!@#$%^&*()"))
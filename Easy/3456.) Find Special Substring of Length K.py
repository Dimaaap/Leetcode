def has_special_substring(s: str, k: int) -> bool:
    """
    You are given a string s and an integer k.

    Determine if there exists a substring of length exactly k in s that satisfies the following conditions:

        The substring consists of only one distinct character (e.g., "aaa" or "bbb").
        If there is a character immediately before the substring, it must be different from the character
        in the substring.
        If there is a character immediately after the substring, it must also be different from the character
        in the substring.

    Return true if such a substring exists. Otherwise, return false.
    """
    n = len(s)

    if k > n:
        return False

    for i in range(n - k + 1):
        x = True
        for j in s[i:i + k]:
            if j != s[i]:
                x = False
                break
        if x and (i == 0 or s[i - 1] != s[i]) and (i + k == n or s[i + k] != s[i]):
            return True

    return False


print(has_special_substring("aaabaaa", 3))
print(has_special_substring("abc", 2))
print(has_special_substring("ccc", 2))
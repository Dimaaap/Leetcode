def find_matching_index(s: str) -> int:
    """
    You are given a string s of length n consisting of lowercase English letters.
    Return the smallest index i such that s[i] == s[n - i - 1].
    If no such index exists, return -1.
    """

    i = 0

    while i < len(s):
        if s[i] == s[len(s) - i - 1]:
            return i
        i += 1
    return -1


print(find_matching_index("abcacbd"))
print(find_matching_index("abc"))
print(find_matching_index("abcdab"))
def merge_alternately(word1: str, word2: str):
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
    starting with word1. If a string is longer than the other, append the additional letters onto
    the end of the merged string.
    Return the merged string.
    """
    res = ""
    i = j = 0
    while i < len(word1) and j < len(word2):
        res += f"{word1[i]}{word2[j]}"
        i += 1
        j += 1
    if j < len(word2):
        res += word2[j:]
    if i < len(word1):
        res += word1[i:]
    return res


print(merge_alternately("abc", "pqr"))
print(merge_alternately("ab", "pqrs"))
print(merge_alternately("abcd", "pq"))

def find_permutation_difference(s: str, t: str):
    """
    You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
    The permutation difference between s and t is defined as the sum of the absolute difference between
    the index of the occurrence of each character in s and the index of the occurrence of the same character in t.
    Return the permutation difference between s and t.
    """
    result = 0
    for index, char in enumerate(s):
        diff = abs(index - t.index(char))
        result += diff
    return result


print(find_permutation_difference("abc", "bac"))
print(find_permutation_difference("abcde", "edbac"))
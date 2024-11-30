def find_lus_length(a: str, b: str) -> int:
    """
    Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
    If no such uncommon subsequence exists, return -1.

    An uncommon subsequence between two strings is a string that is a  subsequence of exactly one of them.
    """
    if a == b:
        return -1
    return max(len(a), len(b))


print(find_lus_length("aba", "cdc"))
print(find_lus_length("aaa", "bbb"))
print(find_lus_length("aaa", "aaa"))

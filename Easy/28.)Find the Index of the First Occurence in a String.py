def str_str(haystack: str, needle: str):
    """
    Given two strings needle and haystack, return the index of the first occurrence
    of needle in haystack, or -1 if needle is not part of haystack
    """
    return haystack.find(needle)


print(str_str("sadbutsad", "sad"))
print(str_str("leetcode", "leeto"))

def str_str(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


print(str_str("sadbutsad", "sad"))
print(str_str("leetcode", "leeto"))
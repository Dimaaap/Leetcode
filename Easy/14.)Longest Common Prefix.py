def longest_common_prefix(strs: list[str]):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    sorted_strs = sorted(strs, key=lambda string: len(string))
    i = sorted_strs[0]
    while i:
        if all(j.startswith(i) for j in strs):
            return i
        else:
            i = i[:-1]
    return i or ''


print(longest_common_prefix(['flower', 'flow', 'flight']))
print(longest_common_prefix(['dog', 'racecar', 'car']))

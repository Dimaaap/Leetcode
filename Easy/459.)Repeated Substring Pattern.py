def repeated_substring_pattern(s: str):
    if len(s) < 2:
        return False
    set_s = set(s)
    count_set = {s.count(i) for i in set_s}
    return len(count_set) == 1


print(repeated_substring_pattern("abab"))
print(repeated_substring_pattern("aba"))
print(repeated_substring_pattern("abcabcabcabc"))
print(repeated_substring_pattern("a"))
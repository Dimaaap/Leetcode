def maximum_length(s: str) -> int:
    """
    You are given a string s that consists of lowercase English letters.

    A string is called special if it is made up of only a single character. For example, the string "abc" is
    not special, whereas the strings "ddd", "zz", and "f" are special.

    Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special
    substring occurs at least thrice.

    A substring is a contiguous non-empty sequence of characters within a string.
    """
    i = j = 0
    max_sub = ""
    max_sub_len = 0
    while i < len(s):
        while j < len(s):
            counter = 0
            substring = s[i:j+1]
            set_substring = set(substring)
            if len(set_substring) == 1:
                for k in range(i, len(s)):
                    if s[k:k+len(substring)] == substring:
                        counter += 1
            if counter == 3:
                max_sub = max(max_sub, substring)
                max_sub_len = max(max_sub_len, len(substring))
            j += 1
        i += 1
        j = i
    return max_sub_len or -1

print(maximum_length("aaaa"))
print(maximum_length("abcdef"))
print(maximum_length("abcaba"))
print(maximum_length("fafff"))
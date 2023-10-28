def length_of_longest_substring(s: str):
    l, longest_substring = 0, 0
    window_chars = set()
    for r in range(len(s)):
        while s[r] in window_chars:
            window_chars.remove(s[l])
            l += 1
        window_chars.add(s[r])
        longest_substring = max(longest_substring, (r - l + 1))
    return longest_substring


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring(""))
print(length_of_longest_substring("aab"))

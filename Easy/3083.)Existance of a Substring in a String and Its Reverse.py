def is_substring_present(s: str):
    reverse_s = s[::-1]
    for i in range(len(s)-1):
        if s[i:i+2] in reverse_s:
            return True
    return False


print(is_substring_present("leetcode"))
print(is_substring_present("abcba"))

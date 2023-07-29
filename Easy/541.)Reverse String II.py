def reverse_str(s: str, k: int):
    s = list(s)
    i = 0
    while i < len(s) - k:
        s[i], s[i + k-1] = s[i + k-1], s[i]
        i += k + k
    return ''.join(s)


print(reverse_str("abcdefg", 2))
print(reverse_str("abcd", 2))
print(reverse_str("abcdef", 3))
print(reverse_str("abcd", 4))
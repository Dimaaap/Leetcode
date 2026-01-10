def reverse_prefix(s: str, k: int) -> str:
    """
    You are given a string s and an integer k.
    Reverse the first k characters of s and return the resulting string.
    """
    pref, rest = s[:k], s[k:]

    pref = pref[::-1]
    return f"{pref}{rest}"


print(reverse_prefix("abcd", 2))
print(reverse_prefix("xyz", 3))
print(reverse_prefix("hey", 1))
def trim_trailing_vowels(s: str) -> str:
    """
    You are given a string s that consists of lowercase English letters.
    Return the string obtained by removing all trailing vowels from s.
    The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.
    """

    vowels = "aeiou"
    s = list(s)

    i = len(s) - 1
    while True:
        if s and s[i] in vowels:
            s = s[:i]
            i -= 1
        else:
            break
    return "".join(s)


print(trim_trailing_vowels("idea"))
print(trim_trailing_vowels("day"))
print(trim_trailing_vowels("aeiou"))

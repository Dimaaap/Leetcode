def reverse_vowels(s: str):
    """
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
    """
    s = list(s)
    vowels = "aeiouAEIOU"
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in vowels:
            j -= 1
        elif s[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return "".join(s)



print(reverse_vowels("hello"))
print(reverse_vowels("leetcode"))
print(reverse_vowels(("aA")))
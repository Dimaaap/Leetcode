import math


def vowel_consonant_score(s: str) -> int:
    """
    You are given a string s consisting of lowercase English letters, spaces, and digits.
    Let v be the number of vowels in s and c be the number of consonants in s.
    A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u', while any other letter in the English alphabet is
    considered a consonant.
    The score of the string s is defined as follows:
        If c > 0, the score = floor(v / c) where floor denotes rounding down to the nearest integer.
        Otherwise, the score = 0.
    Return an integer denoting the score of the string.
    """

    vowels = "aeiou"
    v = c = 0

    for i in s:
        if i in vowels:
            v += 1
        else:
            if i.isalpha():
                c += 1

    if c > 0:
        return math.floor(v / c)
    else:
        return 0


print(vowel_consonant_score("cooear"))
print(vowel_consonant_score("axeyizou"))
print(vowel_consonant_score("au 123"))
print(vowel_consonant_score("i3"))
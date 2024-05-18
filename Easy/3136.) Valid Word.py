from string import ascii_lowercase


def is_valid(word: str):
    """
    A word is considered valid if:
        It contains a minimum of 3 characters.
        It contains only digits (0-9), and English letters (uppercase and lowercase).
        It includes at least one vowel.
        It includes at least one consonant.
    You are given a string word.
    Return true if word is valid, otherwise, return false.
    Notes:
    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.
    """
    word = word.lower()
    vowels = "aeiou"
    consonant = ''.join(i for i in ascii_lowercase if i not in vowels)
    if len(word) < 3:
        return False
    vowels_count = len(set(vowels) & set(word))
    if not vowels_count:
        return False
    consonant_count = len(set(consonant) & set(word))
    if not consonant_count:
        return False
    for i in word:
        if not i.isalnum():
            return False
    return True


print(is_valid("234Adas"))
print(is_valid("b3"))
print(is_valid("a3$e"))

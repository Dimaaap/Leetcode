from string import ascii_lowercase


def check_if_pangram(sentence: str):
    """
    A pangram is a sentence where every letter of the English alphabet appears at least once.
    Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
    or false otherwise.
    """
    letters = set(ascii_lowercase)
    for letter in letters:
        if letter not in sentence:
            return False
    return True


print(check_if_pangram("thequickbrownfoxjumpsoverthelazydog"))
print(check_if_pangram("leetcode"))
